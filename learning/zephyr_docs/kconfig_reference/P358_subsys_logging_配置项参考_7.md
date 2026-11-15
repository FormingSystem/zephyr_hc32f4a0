---
id: learning.zephyr-docs.kconfig-reference.page-358
title: "`subsys/logging`配置项参考（7/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第358章\_`subsys/logging`配置项参考（7/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_BT_MESH_CDB_LOG_LEVEL_WRN"></a>

## 358.1 `CONFIG_BT_MESH_CDB_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_CDB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配置数据库（Configuration database）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CDB_LOG_LEVEL_CHOICE`](P357_subsys_logging_配置项参考_6.md#CONFIG_BT_MESH_CDB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_CFG_LOG_LEVEL_CHOICE"></a>

## 358.2 `CONFIG_BT_MESH_CFG_LOG_LEVEL_CHOICE`

**提示（Prompt）**：配置（Configuration）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_MESH && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_CFG_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MESH_CFG_LOG_LEVEL_INHERIT
CONFIG_BT_MESH_CFG_LOG_LEVEL_OFF
CONFIG_BT_MESH_CFG_LOG_LEVEL_ERR
CONFIG_BT_MESH_CFG_LOG_LEVEL_WRN
CONFIG_BT_MESH_CFG_LOG_LEVEL_INF
CONFIG_BT_MESH_CFG_LOG_LEVEL_DBG
CONFIG_BT_MESH_CFG_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_CFG_LOG_LEVEL_DEFAULT`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CFG_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MESH_CFG_LOG_LEVEL_INHERIT`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CFG_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MESH_CFG_LOG_LEVEL_OFF`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CFG_LOG_LEVEL_OFF)、[`CONFIG_BT_MESH_CFG_LOG_LEVEL_ERR`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CFG_LOG_LEVEL_ERR)、[`CONFIG_BT_MESH_CFG_LOG_LEVEL_WRN`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CFG_LOG_LEVEL_WRN)、[`CONFIG_BT_MESH_CFG_LOG_LEVEL_INF`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CFG_LOG_LEVEL_INF)、[`CONFIG_BT_MESH_CFG_LOG_LEVEL_DBG`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CFG_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MESH_CFG_LOG_LEVEL_DBG"></a>

## 358.3 `CONFIG_BT_MESH_CFG_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_CFG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配置（Configuration）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CFG_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CFG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_CFG_LOG_LEVEL_DEFAULT"></a>

## 358.4 `CONFIG_BT_MESH_CFG_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_CFG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配置（Configuration）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CFG_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CFG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_CFG_LOG_LEVEL_ERR"></a>

## 358.5 `CONFIG_BT_MESH_CFG_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_CFG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配置（Configuration）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CFG_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CFG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_CFG_LOG_LEVEL_INF"></a>

## 358.6 `CONFIG_BT_MESH_CFG_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_CFG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配置（Configuration）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CFG_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CFG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_CFG_LOG_LEVEL_INHERIT"></a>

## 358.7 `CONFIG_BT_MESH_CFG_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_CFG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 选择项（Choice）：`BT_MESH_CFG_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CFG_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CFG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_CFG_LOG_LEVEL_OFF"></a>

## 358.8 `CONFIG_BT_MESH_CFG_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_CFG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配置（Configuration）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CFG_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CFG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_CFG_LOG_LEVEL_WRN"></a>

## 358.9 `CONFIG_BT_MESH_CFG_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_CFG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配置（Configuration）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CFG_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CFG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_CHOICE"></a>

## 358.10 `CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_CHOICE`

**提示（Prompt）**：密码处理（Crypto）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_MESH && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_INHERIT
CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_OFF
CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_ERR
CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_WRN
CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_INF
CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_DBG
CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_DEFAULT`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_INHERIT`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_OFF`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_OFF)、[`CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_ERR`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_ERR)、[`CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_WRN`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_WRN)、[`CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_INF`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_INF)、[`CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_DBG`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_DBG"></a>

## 358.11 `CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 密码处理（Crypto）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_DEFAULT"></a>

## 358.12 `CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 密码处理（Crypto）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_ERR"></a>

## 358.13 `CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 密码处理（Crypto）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_INF"></a>

## 358.14 `CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 密码处理（Crypto）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_INHERIT"></a>

## 358.15 `CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 选择项（Choice）：`BT_MESH_CRYPTO_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_OFF"></a>

## 358.16 `CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 密码处理（Crypto）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_WRN"></a>

## 358.17 `CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 密码处理（Crypto）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_CRYPTO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_DFU_LOG_LEVEL_CHOICE"></a>

## 358.18 `CONFIG_BT_MESH_DFU_LOG_LEVEL_CHOICE`

**提示（Prompt）**：设备固件更新模型（DFU model）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_MESH && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_DFU_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MESH_DFU_LOG_LEVEL_INHERIT
CONFIG_BT_MESH_DFU_LOG_LEVEL_OFF
CONFIG_BT_MESH_DFU_LOG_LEVEL_ERR
CONFIG_BT_MESH_DFU_LOG_LEVEL_WRN
CONFIG_BT_MESH_DFU_LOG_LEVEL_INF
CONFIG_BT_MESH_DFU_LOG_LEVEL_DBG
CONFIG_BT_MESH_DFU_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_DFU_LOG_LEVEL_DEFAULT`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_DFU_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MESH_DFU_LOG_LEVEL_INHERIT`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_DFU_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MESH_DFU_LOG_LEVEL_OFF`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_DFU_LOG_LEVEL_OFF)、[`CONFIG_BT_MESH_DFU_LOG_LEVEL_ERR`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_DFU_LOG_LEVEL_ERR)、[`CONFIG_BT_MESH_DFU_LOG_LEVEL_WRN`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_DFU_LOG_LEVEL_WRN)、[`CONFIG_BT_MESH_DFU_LOG_LEVEL_INF`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_DFU_LOG_LEVEL_INF)、[`CONFIG_BT_MESH_DFU_LOG_LEVEL_DBG`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_DFU_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MESH_DFU_LOG_LEVEL_DBG"></a>

## 358.19 `CONFIG_BT_MESH_DFU_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_DFU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 设备固件更新模型（DFU model）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_DFU_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_DFU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_DFU_LOG_LEVEL_DEFAULT"></a>

## 358.20 `CONFIG_BT_MESH_DFU_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_DFU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 设备固件更新模型（DFU model）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_DFU_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_DFU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_DFU_LOG_LEVEL_ERR"></a>

## 358.21 `CONFIG_BT_MESH_DFU_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_DFU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 设备固件更新模型（DFU model）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_DFU_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_DFU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_DFU_LOG_LEVEL_INF"></a>

## 358.22 `CONFIG_BT_MESH_DFU_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_DFU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 设备固件更新模型（DFU model）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_DFU_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_DFU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_DFU_LOG_LEVEL_INHERIT"></a>

## 358.23 `CONFIG_BT_MESH_DFU_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_DFU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 选择项（Choice）：`BT_MESH_DFU_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_DFU_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_DFU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_DFU_LOG_LEVEL_OFF"></a>

## 358.24 `CONFIG_BT_MESH_DFU_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_DFU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 设备固件更新模型（DFU model）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_DFU_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_DFU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_DFU_LOG_LEVEL_WRN"></a>

## 358.25 `CONFIG_BT_MESH_DFU_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_DFU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 设备固件更新模型（DFU model）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_DFU_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_DFU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_FRIEND_LOG_LEVEL_CHOICE"></a>

## 358.26 `CONFIG_BT_MESH_FRIEND_LOG_LEVEL_CHOICE`

**提示（Prompt）**：友谊节点（Friend）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_MESH && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_FRIEND_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MESH_FRIEND_LOG_LEVEL_INHERIT
CONFIG_BT_MESH_FRIEND_LOG_LEVEL_OFF
CONFIG_BT_MESH_FRIEND_LOG_LEVEL_ERR
CONFIG_BT_MESH_FRIEND_LOG_LEVEL_WRN
CONFIG_BT_MESH_FRIEND_LOG_LEVEL_INF
CONFIG_BT_MESH_FRIEND_LOG_LEVEL_DBG
CONFIG_BT_MESH_FRIEND_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_FRIEND_LOG_LEVEL_DEFAULT`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_FRIEND_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MESH_FRIEND_LOG_LEVEL_INHERIT`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_FRIEND_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MESH_FRIEND_LOG_LEVEL_OFF`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_FRIEND_LOG_LEVEL_OFF)、[`CONFIG_BT_MESH_FRIEND_LOG_LEVEL_ERR`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_FRIEND_LOG_LEVEL_ERR)、[`CONFIG_BT_MESH_FRIEND_LOG_LEVEL_WRN`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_FRIEND_LOG_LEVEL_WRN)、[`CONFIG_BT_MESH_FRIEND_LOG_LEVEL_INF`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_FRIEND_LOG_LEVEL_INF)、[`CONFIG_BT_MESH_FRIEND_LOG_LEVEL_DBG`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_FRIEND_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MESH_FRIEND_LOG_LEVEL_DBG"></a>

## 358.27 `CONFIG_BT_MESH_FRIEND_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_FRIEND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 友谊节点（Friend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_FRIEND_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_FRIEND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_FRIEND_LOG_LEVEL_DEFAULT"></a>

## 358.28 `CONFIG_BT_MESH_FRIEND_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_FRIEND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 友谊节点（Friend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_FRIEND_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_FRIEND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_FRIEND_LOG_LEVEL_ERR"></a>

## 358.29 `CONFIG_BT_MESH_FRIEND_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_FRIEND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 友谊节点（Friend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_FRIEND_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_FRIEND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_FRIEND_LOG_LEVEL_INF"></a>

## 358.30 `CONFIG_BT_MESH_FRIEND_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_FRIEND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 友谊节点（Friend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_FRIEND_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_FRIEND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_FRIEND_LOG_LEVEL_INHERIT"></a>

## 358.31 `CONFIG_BT_MESH_FRIEND_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_FRIEND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 选择项（Choice）：`BT_MESH_FRIEND_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_FRIEND_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_FRIEND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_FRIEND_LOG_LEVEL_OFF"></a>

## 358.32 `CONFIG_BT_MESH_FRIEND_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_FRIEND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 友谊节点（Friend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_FRIEND_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_FRIEND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_FRIEND_LOG_LEVEL_WRN"></a>

## 358.33 `CONFIG_BT_MESH_FRIEND_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_FRIEND_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 友谊节点（Friend）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_FRIEND_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_FRIEND_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_KEYS_LOG_LEVEL_CHOICE"></a>

## 358.34 `CONFIG_BT_MESH_KEYS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：密钥管理（Key management）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_MESH && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_KEYS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MESH_KEYS_LOG_LEVEL_INHERIT
CONFIG_BT_MESH_KEYS_LOG_LEVEL_OFF
CONFIG_BT_MESH_KEYS_LOG_LEVEL_ERR
CONFIG_BT_MESH_KEYS_LOG_LEVEL_WRN
CONFIG_BT_MESH_KEYS_LOG_LEVEL_INF
CONFIG_BT_MESH_KEYS_LOG_LEVEL_DBG
CONFIG_BT_MESH_KEYS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_KEYS_LOG_LEVEL_DEFAULT`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_KEYS_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MESH_KEYS_LOG_LEVEL_INHERIT`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_KEYS_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MESH_KEYS_LOG_LEVEL_OFF`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_KEYS_LOG_LEVEL_OFF)、[`CONFIG_BT_MESH_KEYS_LOG_LEVEL_ERR`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_KEYS_LOG_LEVEL_ERR)、[`CONFIG_BT_MESH_KEYS_LOG_LEVEL_WRN`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_KEYS_LOG_LEVEL_WRN)、[`CONFIG_BT_MESH_KEYS_LOG_LEVEL_INF`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_KEYS_LOG_LEVEL_INF)、[`CONFIG_BT_MESH_KEYS_LOG_LEVEL_DBG`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_KEYS_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MESH_KEYS_LOG_LEVEL_DBG"></a>

## 358.35 `CONFIG_BT_MESH_KEYS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_KEYS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 密钥管理（Key management）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_KEYS_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_KEYS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_KEYS_LOG_LEVEL_DEFAULT"></a>

## 358.36 `CONFIG_BT_MESH_KEYS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_KEYS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 密钥管理（Key management）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_KEYS_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_KEYS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_KEYS_LOG_LEVEL_ERR"></a>

## 358.37 `CONFIG_BT_MESH_KEYS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_KEYS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 密钥管理（Key management）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_KEYS_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_KEYS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_KEYS_LOG_LEVEL_INF"></a>

## 358.38 `CONFIG_BT_MESH_KEYS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_KEYS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 密钥管理（Key management）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_KEYS_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_KEYS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_KEYS_LOG_LEVEL_INHERIT"></a>

## 358.39 `CONFIG_BT_MESH_KEYS_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_KEYS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 选择项（Choice）：`BT_MESH_KEYS_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_KEYS_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_KEYS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_KEYS_LOG_LEVEL_OFF"></a>

## 358.40 `CONFIG_BT_MESH_KEYS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_KEYS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 密钥管理（Key management）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_KEYS_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_KEYS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_KEYS_LOG_LEVEL_WRN"></a>

## 358.41 `CONFIG_BT_MESH_KEYS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_KEYS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 密钥管理（Key management）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_KEYS_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_KEYS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_LOG_LEVEL_CHOICE"></a>

## 358.42 `CONFIG_BT_MESH_LOG_LEVEL_CHOICE`

**提示（Prompt）**：调试日志（Debug logs）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_MESH && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MESH_LOG_LEVEL_INHERIT
CONFIG_BT_MESH_LOG_LEVEL_OFF
CONFIG_BT_MESH_LOG_LEVEL_ERR
CONFIG_BT_MESH_LOG_LEVEL_WRN
CONFIG_BT_MESH_LOG_LEVEL_INF
CONFIG_BT_MESH_LOG_LEVEL_DBG
CONFIG_BT_MESH_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_LOG_LEVEL_DEFAULT`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MESH_LOG_LEVEL_INHERIT`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MESH_LOG_LEVEL_OFF`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOG_LEVEL_OFF)、[`CONFIG_BT_MESH_LOG_LEVEL_ERR`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOG_LEVEL_ERR)、[`CONFIG_BT_MESH_LOG_LEVEL_WRN`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOG_LEVEL_WRN)、[`CONFIG_BT_MESH_LOG_LEVEL_INF`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOG_LEVEL_INF)、[`CONFIG_BT_MESH_LOG_LEVEL_DBG`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MESH_LOG_LEVEL_DBG"></a>

## 358.43 `CONFIG_BT_MESH_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 调试日志（Debug logs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_LOG_LEVEL_DEFAULT"></a>

## 358.44 `CONFIG_BT_MESH_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 调试日志（Debug logs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_LOG_LEVEL_ERR"></a>

## 358.45 `CONFIG_BT_MESH_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 调试日志（Debug logs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_LOG_LEVEL_INF"></a>

## 358.46 `CONFIG_BT_MESH_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 调试日志（Debug logs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_LOG_LEVEL_INHERIT"></a>

## 358.47 `CONFIG_BT_MESH_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 选择项（Choice）：`BT_MESH_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_LOG_LEVEL_OFF"></a>

## 358.48 `CONFIG_BT_MESH_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 调试日志（Debug logs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_LOG_LEVEL_WRN"></a>

## 358.49 `CONFIG_BT_MESH_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 调试日志（Debug logs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_CHOICE"></a>

## 358.50 `CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：低功耗（Low Power）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_MESH && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_INHERIT
CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_OFF
CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_ERR
CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_WRN
CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_INF
CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_DBG
CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_DEFAULT`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_INHERIT`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_OFF`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_OFF)、[`CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_ERR`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_ERR)、[`CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_WRN`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_WRN)、[`CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_INF`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_INF)、[`CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_DBG`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_DBG"></a>

## 358.51 `CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 低功耗（Low Power）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_DEFAULT"></a>

## 358.52 `CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 低功耗（Low Power）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_ERR"></a>

## 358.53 `CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 低功耗（Low Power）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_INF"></a>

## 358.54 `CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 低功耗（Low Power）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_INHERIT"></a>

## 358.55 `CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 选择项（Choice）：`BT_MESH_LOW_POWER_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_OFF"></a>

## 358.56 `CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 低功耗（Low Power）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_WRN"></a>

## 358.57 `CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 低功耗（Low Power）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_LOW_POWER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_MODEL_LOG_LEVEL_CHOICE"></a>

## 358.58 `CONFIG_BT_MESH_MODEL_LOG_LEVEL_CHOICE`

**提示（Prompt）**：基础模型（Foundation model）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_MESH && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_MODEL_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MESH_MODEL_LOG_LEVEL_INHERIT
CONFIG_BT_MESH_MODEL_LOG_LEVEL_OFF
CONFIG_BT_MESH_MODEL_LOG_LEVEL_ERR
CONFIG_BT_MESH_MODEL_LOG_LEVEL_WRN
CONFIG_BT_MESH_MODEL_LOG_LEVEL_INF
CONFIG_BT_MESH_MODEL_LOG_LEVEL_DBG
CONFIG_BT_MESH_MODEL_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_MODEL_LOG_LEVEL_DEFAULT`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_MODEL_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MESH_MODEL_LOG_LEVEL_INHERIT`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_MODEL_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MESH_MODEL_LOG_LEVEL_OFF`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_MODEL_LOG_LEVEL_OFF)、[`CONFIG_BT_MESH_MODEL_LOG_LEVEL_ERR`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_MODEL_LOG_LEVEL_ERR)、[`CONFIG_BT_MESH_MODEL_LOG_LEVEL_WRN`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_MODEL_LOG_LEVEL_WRN)、[`CONFIG_BT_MESH_MODEL_LOG_LEVEL_INF`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_MODEL_LOG_LEVEL_INF)、[`CONFIG_BT_MESH_MODEL_LOG_LEVEL_DBG`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_MODEL_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MESH_MODEL_LOG_LEVEL_DBG"></a>

## 358.59 `CONFIG_BT_MESH_MODEL_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_MODEL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 基础模型（Foundation model）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_MODEL_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_MODEL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_MODEL_LOG_LEVEL_DEFAULT"></a>

## 358.60 `CONFIG_BT_MESH_MODEL_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_MODEL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 基础模型（Foundation model）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_MODEL_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_MODEL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_MODEL_LOG_LEVEL_ERR"></a>

## 358.61 `CONFIG_BT_MESH_MODEL_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_MODEL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 基础模型（Foundation model）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_MODEL_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_MODEL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_MODEL_LOG_LEVEL_INF"></a>

## 358.62 `CONFIG_BT_MESH_MODEL_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_MODEL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 基础模型（Foundation model）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_MODEL_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_MODEL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_MODEL_LOG_LEVEL_INHERIT"></a>

## 358.63 `CONFIG_BT_MESH_MODEL_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_MODEL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 选择项（Choice）：`BT_MESH_MODEL_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_MODEL_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_MODEL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_MODEL_LOG_LEVEL_OFF"></a>

## 358.64 `CONFIG_BT_MESH_MODEL_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_MODEL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 基础模型（Foundation model）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_MODEL_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_MODEL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_MODEL_LOG_LEVEL_WRN"></a>

## 358.65 `CONFIG_BT_MESH_MODEL_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_MODEL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 基础模型（Foundation model）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_MODEL_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_MODEL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_NET_LOG_LEVEL_CHOICE"></a>

## 358.66 `CONFIG_BT_MESH_NET_LOG_LEVEL_CHOICE`

**提示（Prompt）**：网络层（Network layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_MESH && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_NET_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MESH_NET_LOG_LEVEL_INHERIT
CONFIG_BT_MESH_NET_LOG_LEVEL_OFF
CONFIG_BT_MESH_NET_LOG_LEVEL_ERR
CONFIG_BT_MESH_NET_LOG_LEVEL_WRN
CONFIG_BT_MESH_NET_LOG_LEVEL_INF
CONFIG_BT_MESH_NET_LOG_LEVEL_DBG
CONFIG_BT_MESH_NET_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_NET_LOG_LEVEL_DEFAULT`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_NET_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MESH_NET_LOG_LEVEL_INHERIT`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_NET_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MESH_NET_LOG_LEVEL_OFF`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_NET_LOG_LEVEL_OFF)、[`CONFIG_BT_MESH_NET_LOG_LEVEL_ERR`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_NET_LOG_LEVEL_ERR)、[`CONFIG_BT_MESH_NET_LOG_LEVEL_WRN`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_NET_LOG_LEVEL_WRN)、[`CONFIG_BT_MESH_NET_LOG_LEVEL_INF`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_NET_LOG_LEVEL_INF)、[`CONFIG_BT_MESH_NET_LOG_LEVEL_DBG`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_NET_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MESH_NET_LOG_LEVEL_DBG"></a>

## 358.67 `CONFIG_BT_MESH_NET_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_NET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 网络层（Network layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_NET_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_NET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_NET_LOG_LEVEL_DEFAULT"></a>

## 358.68 `CONFIG_BT_MESH_NET_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_NET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 网络层（Network layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_NET_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_NET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_NET_LOG_LEVEL_ERR"></a>

## 358.69 `CONFIG_BT_MESH_NET_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_NET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 网络层（Network layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_NET_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_NET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_NET_LOG_LEVEL_INF"></a>

## 358.70 `CONFIG_BT_MESH_NET_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_NET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 网络层（Network layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_NET_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_NET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_NET_LOG_LEVEL_INHERIT"></a>

## 358.71 `CONFIG_BT_MESH_NET_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_NET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 选择项（Choice）：`BT_MESH_NET_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_NET_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_NET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_NET_LOG_LEVEL_OFF"></a>

## 358.72 `CONFIG_BT_MESH_NET_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_NET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 网络层（Network layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_NET_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_NET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_NET_LOG_LEVEL_WRN"></a>

## 358.73 `CONFIG_BT_MESH_NET_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_NET_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 网络层（Network layer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_NET_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_NET_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_CHOICE"></a>

## 358.74 `CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：配网设备（Provisioning device）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_MESH && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_INHERIT
CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_OFF
CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_ERR
CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_WRN
CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_INF
CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_DBG
CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_DEFAULT`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_INHERIT`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_OFF`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_OFF)、[`CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_ERR`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_ERR)、[`CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_WRN`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_WRN)、[`CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_INF`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_INF)、[`CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_DBG`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_DBG"></a>

## 358.75 `CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配网设备（Provisioning device）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_DEFAULT"></a>

## 358.76 `CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配网设备（Provisioning device）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_ERR"></a>

## 358.77 `CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配网设备（Provisioning device）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_INF"></a>

## 358.78 `CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配网设备（Provisioning device）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_INHERIT"></a>

## 358.79 `CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 选择项（Choice）：`BT_MESH_PROVISIONEE_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_OFF"></a>

## 358.80 `CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配网设备（Provisioning device）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_WRN"></a>

## 358.81 `CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配网设备（Provisioning device）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONEE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_CHOICE"></a>

## 358.82 `CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：配网器（Provisioner）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_MESH && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_INHERIT
CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_OFF
CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_ERR
CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_WRN
CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_INF
CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_DBG
CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_DEFAULT`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_INHERIT`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_OFF`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_OFF)、[`CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_ERR`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_ERR)、[`CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_WRN`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_WRN)、[`CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_INF`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_INF)、[`CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_DBG`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_DBG"></a>

## 358.83 `CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配网器（Provisioner）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_DEFAULT"></a>

## 358.84 `CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配网器（Provisioner）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_ERR"></a>

## 358.85 `CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配网器（Provisioner）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_INF"></a>

## 358.86 `CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配网器（Provisioner）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_INHERIT"></a>

## 358.87 `CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 选择项（Choice）：`BT_MESH_PROVISIONER_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_OFF"></a>

## 358.88 `CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配网器（Provisioner）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_WRN"></a>

## 358.89 `CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配网器（Provisioner）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROVISIONER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROV_LOG_LEVEL_CHOICE"></a>

## 358.90 `CONFIG_BT_MESH_PROV_LOG_LEVEL_CHOICE`

**提示（Prompt）**：配网（Provisioning）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_MESH && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_PROV_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MESH_PROV_LOG_LEVEL_INHERIT
CONFIG_BT_MESH_PROV_LOG_LEVEL_OFF
CONFIG_BT_MESH_PROV_LOG_LEVEL_ERR
CONFIG_BT_MESH_PROV_LOG_LEVEL_WRN
CONFIG_BT_MESH_PROV_LOG_LEVEL_INF
CONFIG_BT_MESH_PROV_LOG_LEVEL_DBG
CONFIG_BT_MESH_PROV_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_PROV_LOG_LEVEL_DEFAULT`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROV_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MESH_PROV_LOG_LEVEL_INHERIT`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROV_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MESH_PROV_LOG_LEVEL_OFF`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROV_LOG_LEVEL_OFF)、[`CONFIG_BT_MESH_PROV_LOG_LEVEL_ERR`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROV_LOG_LEVEL_ERR)、[`CONFIG_BT_MESH_PROV_LOG_LEVEL_WRN`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROV_LOG_LEVEL_WRN)、[`CONFIG_BT_MESH_PROV_LOG_LEVEL_INF`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROV_LOG_LEVEL_INF)、[`CONFIG_BT_MESH_PROV_LOG_LEVEL_DBG`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROV_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MESH_PROV_LOG_LEVEL_DBG"></a>

## 358.91 `CONFIG_BT_MESH_PROV_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配网（Provisioning）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROV_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROV_LOG_LEVEL_DEFAULT"></a>

## 358.92 `CONFIG_BT_MESH_PROV_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配网（Provisioning）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROV_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROV_LOG_LEVEL_ERR"></a>

## 358.93 `CONFIG_BT_MESH_PROV_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配网（Provisioning）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROV_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROV_LOG_LEVEL_INF"></a>

## 358.94 `CONFIG_BT_MESH_PROV_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配网（Provisioning）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROV_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROV_LOG_LEVEL_INHERIT"></a>

## 358.95 `CONFIG_BT_MESH_PROV_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 选择项（Choice）：`BT_MESH_PROV_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROV_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROV_LOG_LEVEL_OFF"></a>

## 358.96 `CONFIG_BT_MESH_PROV_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配网（Provisioning）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROV_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROV_LOG_LEVEL_WRN"></a>

## 358.97 `CONFIG_BT_MESH_PROV_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROV_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 配网（Provisioning）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROV_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROV_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROXY_LOG_LEVEL_CHOICE"></a>

## 358.98 `CONFIG_BT_MESH_PROXY_LOG_LEVEL_CHOICE`

**提示（Prompt）**：代理（Proxy）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_BT_MESH && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_BT_MESH_PROXY_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_BT_MESH_PROXY_LOG_LEVEL_INHERIT
CONFIG_BT_MESH_PROXY_LOG_LEVEL_OFF
CONFIG_BT_MESH_PROXY_LOG_LEVEL_ERR
CONFIG_BT_MESH_PROXY_LOG_LEVEL_WRN
CONFIG_BT_MESH_PROXY_LOG_LEVEL_INF
CONFIG_BT_MESH_PROXY_LOG_LEVEL_DBG
CONFIG_BT_MESH_PROXY_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_BT_MESH`](P327_subsys_bluetooth_配置项参考_8.md#CONFIG_BT_MESH)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_BT_MESH_PROXY_LOG_LEVEL_DEFAULT`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROXY_LOG_LEVEL_DEFAULT)、[`CONFIG_BT_MESH_PROXY_LOG_LEVEL_INHERIT`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_PROXY_LOG_LEVEL_INHERIT)、[`CONFIG_BT_MESH_PROXY_LOG_LEVEL_OFF`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_PROXY_LOG_LEVEL_OFF)、[`CONFIG_BT_MESH_PROXY_LOG_LEVEL_ERR`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_PROXY_LOG_LEVEL_ERR)、[`CONFIG_BT_MESH_PROXY_LOG_LEVEL_WRN`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_PROXY_LOG_LEVEL_WRN)、[`CONFIG_BT_MESH_PROXY_LOG_LEVEL_INF`](P359_subsys_logging_配置项参考_8.md#CONFIG_BT_MESH_PROXY_LOG_LEVEL_INF)、[`CONFIG_BT_MESH_PROXY_LOG_LEVEL_DBG`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROXY_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_BT_MESH_PROXY_LOG_LEVEL_DBG"></a>

## 358.99 `CONFIG_BT_MESH_PROXY_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROXY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 代理（Proxy）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROXY_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROXY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_BT_MESH_PROXY_LOG_LEVEL_DEFAULT"></a>

## 358.100 `CONFIG_BT_MESH_PROXY_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_BT_MESH_PROXY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 网状网络（Mesh） → 代理（Proxy）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_BT_MESH_PROXY_LOG_LEVEL_CHOICE`](P358_subsys_logging_配置项参考_7.md#CONFIG_BT_MESH_PROXY_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P357_subsys_logging_配置项参考_6.md) · [返回大纲](大纲.md) · [下一章](P359_subsys_logging_配置项参考_8.md)
