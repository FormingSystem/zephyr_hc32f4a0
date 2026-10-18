---
id: learning.zephyr-docs.kconfig-reference.page-357
title: "`subsys/logging`配置项参考（6/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第357章\_`subsys/logging`配置项参考（6/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BT_IAS_LOG_LEVEL_DBG"></a>

## 357.1 `CONFIG_BT_IAS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_IAS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 即时告警服务（IAS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_IAS_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_IAS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_IAS_LOG_LEVEL_DEFAULT"></a>

## 357.2 `CONFIG_BT_IAS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_IAS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 即时告警服务（IAS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_IAS_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_IAS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_IAS_LOG_LEVEL_ERR"></a>

## 357.3 `CONFIG_BT_IAS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_IAS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 即时告警服务（IAS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_IAS_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_IAS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_IAS_LOG_LEVEL_INF"></a>

## 357.4 `CONFIG_BT_IAS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_IAS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 即时告警服务（IAS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_IAS_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_IAS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_IAS_LOG_LEVEL_OFF"></a>

## 357.5 `CONFIG_BT_IAS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_IAS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 即时告警服务（IAS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_IAS_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_IAS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_IAS_LOG_LEVEL_WRN"></a>

## 357.6 `CONFIG_BT_IAS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_IAS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 服务（Services） → 即时告警服务（IAS）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_IAS_LOG_LEVEL_CHOICE`](P356_subsys_logging_配置项参考_5.md#CONFIG_BT_IAS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ISO_LOG_LEVEL_CHOICE"></a>

## 357.7 `CONFIG_BT_ISO_LOG_LEVEL_CHOICE`

**提示（Prompt）**：等时通道（ISO channel）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_ISO && CONFIG_BT_HCI_HOST && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_ISO_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_ISO_LOG_LEVEL_INHERIT
CONFIG_BT_ISO_LOG_LEVEL_OFF
CONFIG_BT_ISO_LOG_LEVEL_ERR
CONFIG_BT_ISO_LOG_LEVEL_WRN
CONFIG_BT_ISO_LOG_LEVEL_INF
CONFIG_BT_ISO_LOG_LEVEL_DBG
CONFIG_BT_ISO_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_ISO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_ISO)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_ISO_LOG_LEVEL_DEFAULT`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_ISO_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_ISO_LOG_LEVEL_INHERIT`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_ISO_LOG_LEVEL_INHERIT)、[`CONFIG_BT_ISO_LOG_LEVEL_OFF`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_ISO_LOG_LEVEL_OFF)、[`CONFIG_BT_ISO_LOG_LEVEL_ERR`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_ISO_LOG_LEVEL_ERR)、[`CONFIG_BT_ISO_LOG_LEVEL_WRN`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_ISO_LOG_LEVEL_WRN)、[`CONFIG_BT_ISO_LOG_LEVEL_INF`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_ISO_LOG_LEVEL_INF)、[`CONFIG_BT_ISO_LOG_LEVEL_DBG`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_ISO_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_ISO`、`CONFIG_BT_HCI_HOST`、`CONFIG_BT_LOG`。

<a id="CONFIG_BT_ISO_LOG_LEVEL_DBG"></a>

## 357.8 `CONFIG_BT_ISO_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ISO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 等时通道（ISO channel）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ISO_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_ISO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ISO_LOG_LEVEL_DEFAULT"></a>

## 357.9 `CONFIG_BT_ISO_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ISO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 等时通道（ISO channel）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ISO_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_ISO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ISO_LOG_LEVEL_ERR"></a>

## 357.10 `CONFIG_BT_ISO_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ISO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 等时通道（ISO channel）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ISO_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_ISO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ISO_LOG_LEVEL_INF"></a>

## 357.11 `CONFIG_BT_ISO_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ISO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 等时通道（ISO channel）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ISO_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_ISO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ISO_LOG_LEVEL_INHERIT"></a>

## 357.12 `CONFIG_BT_ISO_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ISO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 选择项（Choice）：`BT_ISO_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_ISO_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_ISO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ISO_LOG_LEVEL_OFF"></a>

## 357.13 `CONFIG_BT_ISO_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ISO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 等时通道（ISO channel）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ISO_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_ISO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_ISO_LOG_LEVEL_WRN"></a>

## 357.14 `CONFIG_BT_ISO_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_ISO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 等时通道（ISO channel）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_ISO_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_ISO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_KEYS_LOG_LEVEL_CHOICE"></a>

## 357.15 `CONFIG_BT_KEYS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙安全密钥（Bluetooth security keys）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_HCI_HOST && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_KEYS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_KEYS_LOG_LEVEL_INHERIT
CONFIG_BT_KEYS_LOG_LEVEL_OFF
CONFIG_BT_KEYS_LOG_LEVEL_ERR
CONFIG_BT_KEYS_LOG_LEVEL_WRN
CONFIG_BT_KEYS_LOG_LEVEL_INF
CONFIG_BT_KEYS_LOG_LEVEL_DBG
CONFIG_BT_KEYS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_KEYS_LOG_LEVEL_DEFAULT`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_KEYS_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_KEYS_LOG_LEVEL_INHERIT`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_KEYS_LOG_LEVEL_INHERIT)、[`CONFIG_BT_KEYS_LOG_LEVEL_OFF`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_KEYS_LOG_LEVEL_OFF)、[`CONFIG_BT_KEYS_LOG_LEVEL_ERR`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_KEYS_LOG_LEVEL_ERR)、[`CONFIG_BT_KEYS_LOG_LEVEL_WRN`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_KEYS_LOG_LEVEL_WRN)、[`CONFIG_BT_KEYS_LOG_LEVEL_INF`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_KEYS_LOG_LEVEL_INF)、[`CONFIG_BT_KEYS_LOG_LEVEL_DBG`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_KEYS_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_LOG`。

<a id="CONFIG_BT_KEYS_LOG_LEVEL_DBG"></a>

## 357.16 `CONFIG_BT_KEYS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_KEYS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙安全密钥（Bluetooth security keys）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_KEYS_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_KEYS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_KEYS_LOG_LEVEL_DEFAULT"></a>

## 357.17 `CONFIG_BT_KEYS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_KEYS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙安全密钥（Bluetooth security keys）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_KEYS_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_KEYS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_KEYS_LOG_LEVEL_ERR"></a>

## 357.18 `CONFIG_BT_KEYS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_KEYS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙安全密钥（Bluetooth security keys）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_KEYS_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_KEYS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_KEYS_LOG_LEVEL_INF"></a>

## 357.19 `CONFIG_BT_KEYS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_KEYS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙安全密钥（Bluetooth security keys）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_KEYS_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_KEYS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_KEYS_LOG_LEVEL_INHERIT"></a>

## 357.20 `CONFIG_BT_KEYS_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_KEYS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 选择项（Choice）：`BT_KEYS_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_KEYS_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_KEYS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_KEYS_LOG_LEVEL_OFF"></a>

## 357.21 `CONFIG_BT_KEYS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_KEYS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙安全密钥（Bluetooth security keys）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_KEYS_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_KEYS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_KEYS_LOG_LEVEL_WRN"></a>

## 357.22 `CONFIG_BT_KEYS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_KEYS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙安全密钥（Bluetooth security keys）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_KEYS_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_KEYS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_L2CAP_LOG_LEVEL_CHOICE"></a>

## 357.23 `CONFIG_BT_L2CAP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙逻辑链路控制与适配协议（Bluetooth L2CAP）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_HCI_HOST && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_L2CAP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_L2CAP_LOG_LEVEL_INHERIT
CONFIG_BT_L2CAP_LOG_LEVEL_OFF
CONFIG_BT_L2CAP_LOG_LEVEL_ERR
CONFIG_BT_L2CAP_LOG_LEVEL_WRN
CONFIG_BT_L2CAP_LOG_LEVEL_INF
CONFIG_BT_L2CAP_LOG_LEVEL_DBG
CONFIG_BT_L2CAP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_HCI_HOST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_HCI_HOST)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_L2CAP_LOG_LEVEL_DEFAULT`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_L2CAP_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_L2CAP_LOG_LEVEL_INHERIT`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_L2CAP_LOG_LEVEL_INHERIT)、[`CONFIG_BT_L2CAP_LOG_LEVEL_OFF`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_L2CAP_LOG_LEVEL_OFF)、[`CONFIG_BT_L2CAP_LOG_LEVEL_ERR`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_L2CAP_LOG_LEVEL_ERR)、[`CONFIG_BT_L2CAP_LOG_LEVEL_WRN`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_L2CAP_LOG_LEVEL_WRN)、[`CONFIG_BT_L2CAP_LOG_LEVEL_INF`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_L2CAP_LOG_LEVEL_INF)、[`CONFIG_BT_L2CAP_LOG_LEVEL_DBG`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_L2CAP_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_HCI_HOST`、`CONFIG_BT_LOG`。

<a id="CONFIG_BT_L2CAP_LOG_LEVEL_DBG"></a>

## 357.24 `CONFIG_BT_L2CAP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_L2CAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙逻辑链路控制与适配协议（Bluetooth L2CAP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_L2CAP_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_L2CAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_L2CAP_LOG_LEVEL_DEFAULT"></a>

## 357.25 `CONFIG_BT_L2CAP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_L2CAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙逻辑链路控制与适配协议（Bluetooth L2CAP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_L2CAP_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_L2CAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_L2CAP_LOG_LEVEL_ERR"></a>

## 357.26 `CONFIG_BT_L2CAP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_L2CAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙逻辑链路控制与适配协议（Bluetooth L2CAP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_L2CAP_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_L2CAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_L2CAP_LOG_LEVEL_INF"></a>

## 357.27 `CONFIG_BT_L2CAP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_L2CAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙逻辑链路控制与适配协议（Bluetooth L2CAP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_L2CAP_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_L2CAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_L2CAP_LOG_LEVEL_INHERIT"></a>

## 357.28 `CONFIG_BT_L2CAP_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_L2CAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 选择项（Choice）：`BT_L2CAP_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_L2CAP_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_L2CAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_L2CAP_LOG_LEVEL_OFF"></a>

## 357.29 `CONFIG_BT_L2CAP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_L2CAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙逻辑链路控制与适配协议（Bluetooth L2CAP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_L2CAP_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_L2CAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_L2CAP_LOG_LEVEL_WRN"></a>

## 357.30 `CONFIG_BT_L2CAP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_L2CAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 主机（Host） → 蓝牙逻辑链路控制与适配协议（Bluetooth L2CAP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_L2CAP_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_L2CAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_LOG_LEVEL_CHOICE"></a>

## 357.31 `CONFIG_BT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙（Bluetooth）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_LOG_LEVEL_OFF
CONFIG_BT_LOG_LEVEL_ERR
CONFIG_BT_LOG_LEVEL_WRN
CONFIG_BT_LOG_LEVEL_INF
CONFIG_BT_LOG_LEVEL_DBG
CONFIG_BT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_LOG_LEVEL_DEFAULT`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_LOG_LEVEL_OFF`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_LOG_LEVEL_OFF)、[`CONFIG_BT_LOG_LEVEL_ERR`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_LOG_LEVEL_ERR)、[`CONFIG_BT_LOG_LEVEL_WRN`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_LOG_LEVEL_WRN)、[`CONFIG_BT_LOG_LEVEL_INF`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_LOG_LEVEL_INF)、[`CONFIG_BT_LOG_LEVEL_DBG`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_LOG_LEVEL_DBG"></a>

## 357.32 `CONFIG_BT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 蓝牙（Bluetooth）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_LOG_LEVEL_DEFAULT"></a>

## 357.33 `CONFIG_BT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 蓝牙（Bluetooth）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_LOG_LEVEL_ERR"></a>

## 357.34 `CONFIG_BT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 蓝牙（Bluetooth）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_LOG_LEVEL_INF"></a>

## 357.35 `CONFIG_BT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 蓝牙（Bluetooth）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_LOG_LEVEL_OFF"></a>

## 357.36 `CONFIG_BT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 蓝牙（Bluetooth）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_LOG_LEVEL_WRN"></a>

## 357.37 `CONFIG_BT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 蓝牙（Bluetooth）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MAP_LOG_LEVEL_CHOICE"></a>

## 357.38 `CONFIG_BT_MAP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：蓝牙消息访问配置文件（Bluetooth Message Access Profile (MAP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_CLASSIC && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MAP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MAP_LOG_LEVEL_INHERIT
CONFIG_BT_MAP_LOG_LEVEL_OFF
CONFIG_BT_MAP_LOG_LEVEL_ERR
CONFIG_BT_MAP_LOG_LEVEL_WRN
CONFIG_BT_MAP_LOG_LEVEL_INF
CONFIG_BT_MAP_LOG_LEVEL_DBG
CONFIG_BT_MAP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_CLASSIC`](P321_subsys_bluetooth_配置项参考_2.md#CONFIG_BT_CLASSIC)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MAP_LOG_LEVEL_DEFAULT`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MAP_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MAP_LOG_LEVEL_INHERIT`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MAP_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MAP_LOG_LEVEL_OFF`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MAP_LOG_LEVEL_OFF)、[`CONFIG_BT_MAP_LOG_LEVEL_ERR`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MAP_LOG_LEVEL_ERR)、[`CONFIG_BT_MAP_LOG_LEVEL_WRN`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MAP_LOG_LEVEL_WRN)、[`CONFIG_BT_MAP_LOG_LEVEL_INF`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MAP_LOG_LEVEL_INF)、[`CONFIG_BT_MAP_LOG_LEVEL_DBG`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MAP_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MAP_LOG_LEVEL_DBG"></a>

## 357.39 `CONFIG_BT_MAP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙消息访问配置文件（Bluetooth Message Access Profile (MAP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MAP_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MAP_LOG_LEVEL_DEFAULT"></a>

## 357.40 `CONFIG_BT_MAP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙消息访问配置文件（Bluetooth Message Access Profile (MAP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MAP_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MAP_LOG_LEVEL_ERR"></a>

## 357.41 `CONFIG_BT_MAP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙消息访问配置文件（Bluetooth Message Access Profile (MAP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MAP_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MAP_LOG_LEVEL_INF"></a>

## 357.42 `CONFIG_BT_MAP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙消息访问配置文件（Bluetooth Message Access Profile (MAP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MAP_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MAP_LOG_LEVEL_INHERIT"></a>

## 357.43 `CONFIG_BT_MAP_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 选择项（Choice）：`BT_MAP_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MAP_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MAP_LOG_LEVEL_OFF"></a>

## 357.44 `CONFIG_BT_MAP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙消息访问配置文件（Bluetooth Message Access Profile (MAP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MAP_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MAP_LOG_LEVEL_WRN"></a>

## 357.45 `CONFIG_BT_MAP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 经典蓝牙（Bluetooth Classic） → 蓝牙消息访问配置文件（Bluetooth Message Access Profile (MAP)）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MAP_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MCC_LOG_LEVEL_CHOICE"></a>

## 357.46 `CONFIG_BT_MCC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：媒体控制客户端（Media Control Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_MCC && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MCC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MCC_LOG_LEVEL_INHERIT
CONFIG_BT_MCC_LOG_LEVEL_OFF
CONFIG_BT_MCC_LOG_LEVEL_ERR
CONFIG_BT_MCC_LOG_LEVEL_WRN
CONFIG_BT_MCC_LOG_LEVEL_INF
CONFIG_BT_MCC_LOG_LEVEL_DBG
CONFIG_BT_MCC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_MCC`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCC)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MCC_LOG_LEVEL_DEFAULT`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCC_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MCC_LOG_LEVEL_INHERIT`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCC_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MCC_LOG_LEVEL_OFF`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCC_LOG_LEVEL_OFF)、[`CONFIG_BT_MCC_LOG_LEVEL_ERR`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCC_LOG_LEVEL_ERR)、[`CONFIG_BT_MCC_LOG_LEVEL_WRN`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCC_LOG_LEVEL_WRN)、[`CONFIG_BT_MCC_LOG_LEVEL_INF`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCC_LOG_LEVEL_INF)、[`CONFIG_BT_MCC_LOG_LEVEL_DBG`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCC_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MCC_LOG_LEVEL_DBG"></a>

## 357.47 `CONFIG_BT_MCC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MCC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 媒体控制客户端（Media Control Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MCC_LOG_LEVEL_DEFAULT"></a>

## 357.48 `CONFIG_BT_MCC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MCC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 媒体控制客户端（Media Control Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MCC_LOG_LEVEL_ERR"></a>

## 357.49 `CONFIG_BT_MCC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MCC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 媒体控制客户端（Media Control Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MCC_LOG_LEVEL_INF"></a>

## 357.50 `CONFIG_BT_MCC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MCC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 媒体控制客户端（Media Control Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MCC_LOG_LEVEL_INHERIT"></a>

## 357.51 `CONFIG_BT_MCC_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MCC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_MCC_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MCC_LOG_LEVEL_OFF"></a>

## 357.52 `CONFIG_BT_MCC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MCC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 媒体控制客户端（Media Control Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MCC_LOG_LEVEL_WRN"></a>

## 357.53 `CONFIG_BT_MCC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MCC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 媒体控制客户端（Media Control Client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCC_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MCS_LOG_LEVEL_CHOICE"></a>

## 357.54 `CONFIG_BT_MCS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：媒体控制服务（Media Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_MCS && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MCS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MCS_LOG_LEVEL_INHERIT
CONFIG_BT_MCS_LOG_LEVEL_OFF
CONFIG_BT_MCS_LOG_LEVEL_ERR
CONFIG_BT_MCS_LOG_LEVEL_WRN
CONFIG_BT_MCS_LOG_LEVEL_INF
CONFIG_BT_MCS_LOG_LEVEL_DBG
CONFIG_BT_MCS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_MCS`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MCS)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MCS_LOG_LEVEL_DEFAULT`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCS_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MCS_LOG_LEVEL_INHERIT`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCS_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MCS_LOG_LEVEL_OFF`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCS_LOG_LEVEL_OFF)、[`CONFIG_BT_MCS_LOG_LEVEL_ERR`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCS_LOG_LEVEL_ERR)、[`CONFIG_BT_MCS_LOG_LEVEL_WRN`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCS_LOG_LEVEL_WRN)、[`CONFIG_BT_MCS_LOG_LEVEL_INF`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCS_LOG_LEVEL_INF)、[`CONFIG_BT_MCS_LOG_LEVEL_DBG`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCS_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MCS_LOG_LEVEL_DBG"></a>

## 357.55 `CONFIG_BT_MCS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MCS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 媒体控制服务（Media Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCS_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MCS_LOG_LEVEL_DEFAULT"></a>

## 357.56 `CONFIG_BT_MCS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MCS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 媒体控制服务（Media Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCS_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MCS_LOG_LEVEL_ERR"></a>

## 357.57 `CONFIG_BT_MCS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MCS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 媒体控制服务（Media Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCS_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MCS_LOG_LEVEL_INF"></a>

## 357.58 `CONFIG_BT_MCS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MCS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 媒体控制服务（Media Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCS_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MCS_LOG_LEVEL_INHERIT"></a>

## 357.59 `CONFIG_BT_MCS_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MCS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`BT_MCS_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MCS_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MCS_LOG_LEVEL_OFF"></a>

## 357.60 `CONFIG_BT_MCS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MCS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 媒体控制服务（Media Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCS_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MCS_LOG_LEVEL_WRN"></a>

## 357.61 `CONFIG_BT_MCS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MCS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 媒体控制服务（Media Control Service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MCS_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MCS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_ACCESS_LOG_LEVEL_CHOICE"></a>

## 357.62 `CONFIG_BT_MESH_ACCESS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：接入层（Access layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_MESH && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_ACCESS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MESH_ACCESS_LOG_LEVEL_INHERIT
CONFIG_BT_MESH_ACCESS_LOG_LEVEL_OFF
CONFIG_BT_MESH_ACCESS_LOG_LEVEL_ERR
CONFIG_BT_MESH_ACCESS_LOG_LEVEL_WRN
CONFIG_BT_MESH_ACCESS_LOG_LEVEL_INF
CONFIG_BT_MESH_ACCESS_LOG_LEVEL_DBG
CONFIG_BT_MESH_ACCESS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_ACCESS_LOG_LEVEL_DEFAULT`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ACCESS_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MESH_ACCESS_LOG_LEVEL_INHERIT`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ACCESS_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MESH_ACCESS_LOG_LEVEL_OFF`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ACCESS_LOG_LEVEL_OFF)、[`CONFIG_BT_MESH_ACCESS_LOG_LEVEL_ERR`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ACCESS_LOG_LEVEL_ERR)、[`CONFIG_BT_MESH_ACCESS_LOG_LEVEL_WRN`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ACCESS_LOG_LEVEL_WRN)、[`CONFIG_BT_MESH_ACCESS_LOG_LEVEL_INF`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ACCESS_LOG_LEVEL_INF)、[`CONFIG_BT_MESH_ACCESS_LOG_LEVEL_DBG`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ACCESS_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MESH_ACCESS_LOG_LEVEL_DBG"></a>

## 357.63 `CONFIG_BT_MESH_ACCESS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_ACCESS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 接入层（Access layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_ACCESS_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ACCESS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_ACCESS_LOG_LEVEL_DEFAULT"></a>

## 357.64 `CONFIG_BT_MESH_ACCESS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_ACCESS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 接入层（Access layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_ACCESS_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ACCESS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_ACCESS_LOG_LEVEL_ERR"></a>

## 357.65 `CONFIG_BT_MESH_ACCESS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_ACCESS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 接入层（Access layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_ACCESS_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ACCESS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_ACCESS_LOG_LEVEL_INF"></a>

## 357.66 `CONFIG_BT_MESH_ACCESS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_ACCESS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 接入层（Access layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_ACCESS_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ACCESS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_ACCESS_LOG_LEVEL_INHERIT"></a>

## 357.67 `CONFIG_BT_MESH_ACCESS_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_ACCESS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 选择项（Choice）：`BT_MESH_ACCESS_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_ACCESS_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ACCESS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_ACCESS_LOG_LEVEL_OFF"></a>

## 357.68 `CONFIG_BT_MESH_ACCESS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_ACCESS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 接入层（Access layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_ACCESS_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ACCESS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_ACCESS_LOG_LEVEL_WRN"></a>

## 357.69 `CONFIG_BT_MESH_ACCESS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_ACCESS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 接入层（Access layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_ACCESS_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ACCESS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_ADV_LOG_LEVEL_CHOICE"></a>

## 357.70 `CONFIG_BT_MESH_ADV_LOG_LEVEL_CHOICE`

**提示（Prompt）**：广播（Advertising）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_MESH && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_ADV_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MESH_ADV_LOG_LEVEL_INHERIT
CONFIG_BT_MESH_ADV_LOG_LEVEL_OFF
CONFIG_BT_MESH_ADV_LOG_LEVEL_ERR
CONFIG_BT_MESH_ADV_LOG_LEVEL_WRN
CONFIG_BT_MESH_ADV_LOG_LEVEL_INF
CONFIG_BT_MESH_ADV_LOG_LEVEL_DBG
CONFIG_BT_MESH_ADV_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_ADV_LOG_LEVEL_DEFAULT`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ADV_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MESH_ADV_LOG_LEVEL_INHERIT`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ADV_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MESH_ADV_LOG_LEVEL_OFF`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ADV_LOG_LEVEL_OFF)、[`CONFIG_BT_MESH_ADV_LOG_LEVEL_ERR`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ADV_LOG_LEVEL_ERR)、[`CONFIG_BT_MESH_ADV_LOG_LEVEL_WRN`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ADV_LOG_LEVEL_WRN)、[`CONFIG_BT_MESH_ADV_LOG_LEVEL_INF`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ADV_LOG_LEVEL_INF)、[`CONFIG_BT_MESH_ADV_LOG_LEVEL_DBG`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ADV_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MESH_ADV_LOG_LEVEL_DBG"></a>

## 357.71 `CONFIG_BT_MESH_ADV_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_ADV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 广播（Advertising）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_ADV_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ADV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_ADV_LOG_LEVEL_DEFAULT"></a>

## 357.72 `CONFIG_BT_MESH_ADV_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_ADV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 广播（Advertising）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_ADV_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ADV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_ADV_LOG_LEVEL_ERR"></a>

## 357.73 `CONFIG_BT_MESH_ADV_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_ADV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 广播（Advertising）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_ADV_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ADV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_ADV_LOG_LEVEL_INF"></a>

## 357.74 `CONFIG_BT_MESH_ADV_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_ADV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 广播（Advertising）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_ADV_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ADV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_ADV_LOG_LEVEL_INHERIT"></a>

## 357.75 `CONFIG_BT_MESH_ADV_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_ADV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 选择项（Choice）：`BT_MESH_ADV_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_ADV_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ADV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_ADV_LOG_LEVEL_OFF"></a>

## 357.76 `CONFIG_BT_MESH_ADV_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_ADV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 广播（Advertising）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_ADV_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ADV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_ADV_LOG_LEVEL_WRN"></a>

## 357.77 `CONFIG_BT_MESH_ADV_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_ADV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 广播（Advertising）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_ADV_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_ADV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_BEACON_LOG_LEVEL_CHOICE"></a>

## 357.78 `CONFIG_BT_MESH_BEACON_LOG_LEVEL_CHOICE`

**提示（Prompt）**：信标（Beacon）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_MESH && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_BEACON_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MESH_BEACON_LOG_LEVEL_INHERIT
CONFIG_BT_MESH_BEACON_LOG_LEVEL_OFF
CONFIG_BT_MESH_BEACON_LOG_LEVEL_ERR
CONFIG_BT_MESH_BEACON_LOG_LEVEL_WRN
CONFIG_BT_MESH_BEACON_LOG_LEVEL_INF
CONFIG_BT_MESH_BEACON_LOG_LEVEL_DBG
CONFIG_BT_MESH_BEACON_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_BEACON_LOG_LEVEL_DEFAULT`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BEACON_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MESH_BEACON_LOG_LEVEL_INHERIT`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BEACON_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MESH_BEACON_LOG_LEVEL_OFF`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BEACON_LOG_LEVEL_OFF)、[`CONFIG_BT_MESH_BEACON_LOG_LEVEL_ERR`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BEACON_LOG_LEVEL_ERR)、[`CONFIG_BT_MESH_BEACON_LOG_LEVEL_WRN`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BEACON_LOG_LEVEL_WRN)、[`CONFIG_BT_MESH_BEACON_LOG_LEVEL_INF`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BEACON_LOG_LEVEL_INF)、[`CONFIG_BT_MESH_BEACON_LOG_LEVEL_DBG`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BEACON_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MESH_BEACON_LOG_LEVEL_DBG"></a>

## 357.79 `CONFIG_BT_MESH_BEACON_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_BEACON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 信标（Beacon）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BEACON_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BEACON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_BEACON_LOG_LEVEL_DEFAULT"></a>

## 357.80 `CONFIG_BT_MESH_BEACON_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_BEACON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 信标（Beacon）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BEACON_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BEACON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_BEACON_LOG_LEVEL_ERR"></a>

## 357.81 `CONFIG_BT_MESH_BEACON_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_BEACON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 信标（Beacon）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BEACON_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BEACON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_BEACON_LOG_LEVEL_INF"></a>

## 357.82 `CONFIG_BT_MESH_BEACON_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_BEACON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 信标（Beacon）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BEACON_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BEACON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_BEACON_LOG_LEVEL_INHERIT"></a>

## 357.83 `CONFIG_BT_MESH_BEACON_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_BEACON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 选择项（Choice）：`BT_MESH_BEACON_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BEACON_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BEACON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_BEACON_LOG_LEVEL_OFF"></a>

## 357.84 `CONFIG_BT_MESH_BEACON_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_BEACON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 信标（Beacon）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BEACON_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BEACON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_BEACON_LOG_LEVEL_WRN"></a>

## 357.85 `CONFIG_BT_MESH_BEACON_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_BEACON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 信标（Beacon）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BEACON_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BEACON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_BRG_LOG_LEVEL_CHOICE"></a>

## 357.86 `CONFIG_BT_MESH_BRG_LOG_LEVEL_CHOICE`

**提示（Prompt）**：子网桥接层（Subnet Bridging layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_MESH && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_BRG_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MESH_BRG_LOG_LEVEL_INHERIT
CONFIG_BT_MESH_BRG_LOG_LEVEL_OFF
CONFIG_BT_MESH_BRG_LOG_LEVEL_ERR
CONFIG_BT_MESH_BRG_LOG_LEVEL_WRN
CONFIG_BT_MESH_BRG_LOG_LEVEL_INF
CONFIG_BT_MESH_BRG_LOG_LEVEL_DBG
CONFIG_BT_MESH_BRG_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_BRG_LOG_LEVEL_DEFAULT`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BRG_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MESH_BRG_LOG_LEVEL_INHERIT`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BRG_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MESH_BRG_LOG_LEVEL_OFF`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BRG_LOG_LEVEL_OFF)、[`CONFIG_BT_MESH_BRG_LOG_LEVEL_ERR`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BRG_LOG_LEVEL_ERR)、[`CONFIG_BT_MESH_BRG_LOG_LEVEL_WRN`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BRG_LOG_LEVEL_WRN)、[`CONFIG_BT_MESH_BRG_LOG_LEVEL_INF`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BRG_LOG_LEVEL_INF)、[`CONFIG_BT_MESH_BRG_LOG_LEVEL_DBG`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BRG_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MESH_BRG_LOG_LEVEL_DBG"></a>

## 357.87 `CONFIG_BT_MESH_BRG_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_BRG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 子网桥接层（Subnet Bridging layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BRG_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BRG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_BRG_LOG_LEVEL_DEFAULT"></a>

## 357.88 `CONFIG_BT_MESH_BRG_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_BRG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 子网桥接层（Subnet Bridging layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BRG_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BRG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_BRG_LOG_LEVEL_ERR"></a>

## 357.89 `CONFIG_BT_MESH_BRG_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_BRG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 子网桥接层（Subnet Bridging layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BRG_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BRG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_BRG_LOG_LEVEL_INF"></a>

## 357.90 `CONFIG_BT_MESH_BRG_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_BRG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 子网桥接层（Subnet Bridging layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BRG_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BRG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_BRG_LOG_LEVEL_INHERIT"></a>

## 357.91 `CONFIG_BT_MESH_BRG_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_BRG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 选择项（Choice）：`BT_MESH_BRG_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BRG_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BRG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_BRG_LOG_LEVEL_OFF"></a>

## 357.92 `CONFIG_BT_MESH_BRG_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_BRG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 子网桥接层（Subnet Bridging layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BRG_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BRG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_BRG_LOG_LEVEL_WRN"></a>

## 357.93 `CONFIG_BT_MESH_BRG_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_BRG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 子网桥接层（Subnet Bridging layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_BRG_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_BRG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_CDB_LOG_LEVEL_CHOICE"></a>

## 357.94 `CONFIG_BT_MESH_CDB_LOG_LEVEL_CHOICE`

**提示（Prompt）**：配置数据库（Configuration database）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_MESH && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_CDB_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MESH_CDB_LOG_LEVEL_INHERIT
CONFIG_BT_MESH_CDB_LOG_LEVEL_OFF
CONFIG_BT_MESH_CDB_LOG_LEVEL_ERR
CONFIG_BT_MESH_CDB_LOG_LEVEL_WRN
CONFIG_BT_MESH_CDB_LOG_LEVEL_INF
CONFIG_BT_MESH_CDB_LOG_LEVEL_DBG
CONFIG_BT_MESH_CDB_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_CDB_LOG_LEVEL_DEFAULT`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_CDB_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MESH_CDB_LOG_LEVEL_INHERIT`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_CDB_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MESH_CDB_LOG_LEVEL_OFF`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_CDB_LOG_LEVEL_OFF)、[`CONFIG_BT_MESH_CDB_LOG_LEVEL_ERR`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_CDB_LOG_LEVEL_ERR)、[`CONFIG_BT_MESH_CDB_LOG_LEVEL_WRN`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CDB_LOG_LEVEL_WRN)、[`CONFIG_BT_MESH_CDB_LOG_LEVEL_INF`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_CDB_LOG_LEVEL_INF)、[`CONFIG_BT_MESH_CDB_LOG_LEVEL_DBG`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_CDB_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MESH_CDB_LOG_LEVEL_DBG"></a>

## 357.95 `CONFIG_BT_MESH_CDB_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_CDB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配置数据库（Configuration database）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CDB_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_CDB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_CDB_LOG_LEVEL_DEFAULT"></a>

## 357.96 `CONFIG_BT_MESH_CDB_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_CDB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配置数据库（Configuration database）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CDB_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_CDB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_CDB_LOG_LEVEL_ERR"></a>

## 357.97 `CONFIG_BT_MESH_CDB_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_CDB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配置数据库（Configuration database）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CDB_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_CDB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_CDB_LOG_LEVEL_INF"></a>

## 357.98 `CONFIG_BT_MESH_CDB_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_CDB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配置数据库（Configuration database）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CDB_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_CDB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_CDB_LOG_LEVEL_INHERIT"></a>

## 357.99 `CONFIG_BT_MESH_CDB_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_CDB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 选择项（Choice）：`BT_MESH_CDB_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CDB_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_CDB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_CDB_LOG_LEVEL_OFF"></a>

## 357.100 `CONFIG_BT_MESH_CDB_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_CDB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配置数据库（Configuration database）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CDB_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_CDB_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P356_subsys_logging_配置项参考_5.md) · [返回大纲](大纲.md) · [下一章](P358_subsys_logging_配置项参考_7.md)
