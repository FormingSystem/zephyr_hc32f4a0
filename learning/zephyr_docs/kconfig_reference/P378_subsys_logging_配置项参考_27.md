---
id: learning.zephyr-docs.kconfig-reference.page-378
title: "`subsys/logging`配置项参考（27/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第378章\_`subsys/logging`配置项参考（27/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_UDC_DRIVER_LOG_LEVEL_DEFAULT"></a>

## 378.1 `CONFIG_UDC_DRIVER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UDC_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → USB 驱动（usb drv）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_UDC_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UDC_DRIVER_LOG_LEVEL_ERR"></a>

## 378.2 `CONFIG_UDC_DRIVER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UDC_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → USB 驱动（usb drv）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_UDC_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UDC_DRIVER_LOG_LEVEL_INF"></a>

## 378.3 `CONFIG_UDC_DRIVER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UDC_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → USB 驱动（usb drv）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_UDC_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UDC_DRIVER_LOG_LEVEL_OFF"></a>

## 378.4 `CONFIG_UDC_DRIVER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UDC_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → USB 驱动（usb drv）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_UDC_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UDC_DRIVER_LOG_LEVEL_WRN"></a>

## 378.5 `CONFIG_UDC_DRIVER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UDC_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → USB 驱动（usb drv）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_UDC_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UHC_DRIVER_LOG_LEVEL_CHOICE"></a>

## 378.6 `CONFIG_UHC_DRIVER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB 主机控制器驱动（uhc drv）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_UHC_DRIVER
```

**默认值（Defaults）**

```text
CONFIG_UHC_DRIVER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_UHC_DRIVER_LOG_LEVEL_OFF
CONFIG_UHC_DRIVER_LOG_LEVEL_ERR
CONFIG_UHC_DRIVER_LOG_LEVEL_WRN
CONFIG_UHC_DRIVER_LOG_LEVEL_INF
CONFIG_UHC_DRIVER_LOG_LEVEL_DBG
CONFIG_UHC_DRIVER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_UHC_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_UHC_DRIVER)、[`CONFIG_UHC_DRIVER_LOG_LEVEL_DEFAULT`](P378_subsys_logging_配置项参考_27.md#CONFIG_UHC_DRIVER_LOG_LEVEL_DEFAULT)、[`CONFIG_UHC_DRIVER_LOG_LEVEL_OFF`](P378_subsys_logging_配置项参考_27.md#CONFIG_UHC_DRIVER_LOG_LEVEL_OFF)、[`CONFIG_UHC_DRIVER_LOG_LEVEL_ERR`](P378_subsys_logging_配置项参考_27.md#CONFIG_UHC_DRIVER_LOG_LEVEL_ERR)、[`CONFIG_UHC_DRIVER_LOG_LEVEL_WRN`](P378_subsys_logging_配置项参考_27.md#CONFIG_UHC_DRIVER_LOG_LEVEL_WRN)、[`CONFIG_UHC_DRIVER_LOG_LEVEL_INF`](P378_subsys_logging_配置项参考_27.md#CONFIG_UHC_DRIVER_LOG_LEVEL_INF)、[`CONFIG_UHC_DRIVER_LOG_LEVEL_DBG`](P378_subsys_logging_配置项参考_27.md#CONFIG_UHC_DRIVER_LOG_LEVEL_DBG)。

<a id="CONFIG_UHC_DRIVER_LOG_LEVEL_DBG"></a>

## 378.7 `CONFIG_UHC_DRIVER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UHC_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］ → USB 主机控制器驱动（uhc drv）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UHC_DRIVER_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_UHC_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UHC_DRIVER_LOG_LEVEL_DEFAULT"></a>

## 378.8 `CONFIG_UHC_DRIVER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UHC_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］ → USB 主机控制器驱动（uhc drv）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UHC_DRIVER_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_UHC_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UHC_DRIVER_LOG_LEVEL_ERR"></a>

## 378.9 `CONFIG_UHC_DRIVER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UHC_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］ → USB 主机控制器驱动（uhc drv）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UHC_DRIVER_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_UHC_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UHC_DRIVER_LOG_LEVEL_INF"></a>

## 378.10 `CONFIG_UHC_DRIVER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UHC_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］ → USB 主机控制器驱动（uhc drv）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UHC_DRIVER_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_UHC_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UHC_DRIVER_LOG_LEVEL_OFF"></a>

## 378.11 `CONFIG_UHC_DRIVER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UHC_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］ → USB 主机控制器驱动（uhc drv）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UHC_DRIVER_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_UHC_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UHC_DRIVER_LOG_LEVEL_WRN"></a>

## 378.12 `CONFIG_UHC_DRIVER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UHC_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 主机控制器（Host Controller）驱动［实验性，EXPERIMENTAL］ → USB 主机控制器驱动（uhc drv）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UHC_DRIVER_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_UHC_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UPDATEHUB_LOG_LEVEL_CHOICE"></a>

## 378.13 `CONFIG_UPDATEHUB_LOG_LEVEL_CHOICE`

**提示（Prompt）**：UpdateHub 日志（Log level for UpdateHub）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_UPDATEHUB
```

**默认值（Defaults）**

```text
CONFIG_UPDATEHUB_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_UPDATEHUB_LOG_LEVEL_OFF
CONFIG_UPDATEHUB_LOG_LEVEL_ERR
CONFIG_UPDATEHUB_LOG_LEVEL_WRN
CONFIG_UPDATEHUB_LOG_LEVEL_INF
CONFIG_UPDATEHUB_LOG_LEVEL_DBG
CONFIG_UPDATEHUB_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → UpdateHub 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_UPDATEHUB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UPDATEHUB)、[`CONFIG_UPDATEHUB_LOG_LEVEL_DEFAULT`](P378_subsys_logging_配置项参考_27.md#CONFIG_UPDATEHUB_LOG_LEVEL_DEFAULT)、[`CONFIG_UPDATEHUB_LOG_LEVEL_OFF`](P378_subsys_logging_配置项参考_27.md#CONFIG_UPDATEHUB_LOG_LEVEL_OFF)、[`CONFIG_UPDATEHUB_LOG_LEVEL_ERR`](P378_subsys_logging_配置项参考_27.md#CONFIG_UPDATEHUB_LOG_LEVEL_ERR)、[`CONFIG_UPDATEHUB_LOG_LEVEL_WRN`](P378_subsys_logging_配置项参考_27.md#CONFIG_UPDATEHUB_LOG_LEVEL_WRN)、[`CONFIG_UPDATEHUB_LOG_LEVEL_INF`](P378_subsys_logging_配置项参考_27.md#CONFIG_UPDATEHUB_LOG_LEVEL_INF)、[`CONFIG_UPDATEHUB_LOG_LEVEL_DBG`](P378_subsys_logging_配置项参考_27.md#CONFIG_UPDATEHUB_LOG_LEVEL_DBG)。

<a id="CONFIG_UPDATEHUB_LOG_LEVEL_DBG"></a>

## 378.14 `CONFIG_UPDATEHUB_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UPDATEHUB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → UpdateHub 固件空中更新支持（Firmware Over-the-Air） → UpdateHub 日志（Log level for UpdateHub）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UPDATEHUB_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_UPDATEHUB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UPDATEHUB_LOG_LEVEL_DEFAULT"></a>

## 378.15 `CONFIG_UPDATEHUB_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UPDATEHUB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → UpdateHub 固件空中更新支持（Firmware Over-the-Air） → UpdateHub 日志（Log level for UpdateHub）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UPDATEHUB_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_UPDATEHUB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UPDATEHUB_LOG_LEVEL_ERR"></a>

## 378.16 `CONFIG_UPDATEHUB_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UPDATEHUB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → UpdateHub 固件空中更新支持（Firmware Over-the-Air） → UpdateHub 日志（Log level for UpdateHub）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UPDATEHUB_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_UPDATEHUB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UPDATEHUB_LOG_LEVEL_INF"></a>

## 378.17 `CONFIG_UPDATEHUB_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UPDATEHUB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → UpdateHub 固件空中更新支持（Firmware Over-the-Air） → UpdateHub 日志（Log level for UpdateHub）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UPDATEHUB_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_UPDATEHUB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UPDATEHUB_LOG_LEVEL_OFF"></a>

## 378.18 `CONFIG_UPDATEHUB_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UPDATEHUB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → UpdateHub 固件空中更新支持（Firmware Over-the-Air） → UpdateHub 日志（Log level for UpdateHub）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UPDATEHUB_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_UPDATEHUB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UPDATEHUB_LOG_LEVEL_WRN"></a>

## 378.19 `CONFIG_UPDATEHUB_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UPDATEHUB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → UpdateHub 固件空中更新支持（Firmware Over-the-Air） → UpdateHub 日志（Log level for UpdateHub）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UPDATEHUB_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_UPDATEHUB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBC_LOG_LEVEL_CHOICE"></a>

## 378.20 `CONFIG_USBC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB Type-C（usbc）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USBC_TCPC_DRIVER
```

**默认值（Defaults）**

```text
CONFIG_USBC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USBC_LOG_LEVEL_OFF
CONFIG_USBC_LOG_LEVEL_ERR
CONFIG_USBC_LOG_LEVEL_WRN
CONFIG_USBC_LOG_LEVEL_INF
CONFIG_USBC_LOG_LEVEL_DBG
CONFIG_USBC_LOG_LEVEL_DEFAULT
CONFIG_USBC_LOG_LEVEL_OFF
CONFIG_USBC_LOG_LEVEL_ERR
CONFIG_USBC_LOG_LEVEL_WRN
CONFIG_USBC_LOG_LEVEL_INF
CONFIG_USBC_LOG_LEVEL_DBG
CONFIG_USBC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C Type-C 端口控制器（TCPC）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USBC_TCPC_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_TCPC_DRIVER)、[`CONFIG_USBC_LOG_LEVEL_DEFAULT`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_LOG_LEVEL_DEFAULT)、[`CONFIG_USBC_LOG_LEVEL_OFF`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_LOG_LEVEL_OFF)、[`CONFIG_USBC_LOG_LEVEL_ERR`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_LOG_LEVEL_ERR)、[`CONFIG_USBC_LOG_LEVEL_WRN`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_LOG_LEVEL_WRN)、[`CONFIG_USBC_LOG_LEVEL_INF`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_LOG_LEVEL_INF)、[`CONFIG_USBC_LOG_LEVEL_DBG`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_LOG_LEVEL_DBG)。

<a id="CONFIG_USBC_LOG_LEVEL_DBG"></a>

## 378.21 `CONFIG_USBC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C Type-C 端口控制器（TCPC）驱动 → USB Type-C（usbc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBC_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBC_LOG_LEVEL_DEFAULT"></a>

## 378.22 `CONFIG_USBC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C Type-C 端口控制器（TCPC）驱动 → USB Type-C（usbc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBC_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBC_LOG_LEVEL_ERR"></a>

## 378.23 `CONFIG_USBC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C Type-C 端口控制器（TCPC）驱动 → USB Type-C（usbc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBC_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBC_LOG_LEVEL_INF"></a>

## 378.24 `CONFIG_USBC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C Type-C 端口控制器（TCPC）驱动 → USB Type-C（usbc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBC_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBC_LOG_LEVEL_OFF"></a>

## 378.25 `CONFIG_USBC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C Type-C 端口控制器（TCPC）驱动 → USB Type-C（usbc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBC_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBC_LOG_LEVEL_WRN"></a>

## 378.26 `CONFIG_USBC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C Type-C 端口控制器（TCPC）驱动 → USB Type-C（usbc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBC_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBC_PPC_LOG_LEVEL_CHOICE"></a>

## 378.27 `CONFIG_USBC_PPC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB Type-C 电源路径控制器（usbc-ppc）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USBC_PPC_DRIVER
```

**默认值（Defaults）**

```text
CONFIG_USBC_PPC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USBC_PPC_LOG_LEVEL_OFF
CONFIG_USBC_PPC_LOG_LEVEL_ERR
CONFIG_USBC_PPC_LOG_LEVEL_WRN
CONFIG_USBC_PPC_LOG_LEVEL_INF
CONFIG_USBC_PPC_LOG_LEVEL_DBG
CONFIG_USBC_PPC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C 电源路径控制器（PPC）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USBC_PPC_DRIVER`](P181_drivers_usb_c_配置项参考.md#CONFIG_USBC_PPC_DRIVER)、[`CONFIG_USBC_PPC_LOG_LEVEL_DEFAULT`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_PPC_LOG_LEVEL_DEFAULT)、[`CONFIG_USBC_PPC_LOG_LEVEL_OFF`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_PPC_LOG_LEVEL_OFF)、[`CONFIG_USBC_PPC_LOG_LEVEL_ERR`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_PPC_LOG_LEVEL_ERR)、[`CONFIG_USBC_PPC_LOG_LEVEL_WRN`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_PPC_LOG_LEVEL_WRN)、[`CONFIG_USBC_PPC_LOG_LEVEL_INF`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_PPC_LOG_LEVEL_INF)、[`CONFIG_USBC_PPC_LOG_LEVEL_DBG`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_PPC_LOG_LEVEL_DBG)。

<a id="CONFIG_USBC_PPC_LOG_LEVEL_DBG"></a>

## 378.28 `CONFIG_USBC_PPC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBC_PPC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C 电源路径控制器（PPC）驱动 → USB Type-C 电源路径控制器（usbc-ppc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBC_PPC_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_PPC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBC_PPC_LOG_LEVEL_DEFAULT"></a>

## 378.29 `CONFIG_USBC_PPC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBC_PPC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C 电源路径控制器（PPC）驱动 → USB Type-C 电源路径控制器（usbc-ppc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBC_PPC_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_PPC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBC_PPC_LOG_LEVEL_ERR"></a>

## 378.30 `CONFIG_USBC_PPC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBC_PPC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C 电源路径控制器（PPC）驱动 → USB Type-C 电源路径控制器（usbc-ppc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBC_PPC_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_PPC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBC_PPC_LOG_LEVEL_INF"></a>

## 378.31 `CONFIG_USBC_PPC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBC_PPC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C 电源路径控制器（PPC）驱动 → USB Type-C 电源路径控制器（usbc-ppc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBC_PPC_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_PPC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBC_PPC_LOG_LEVEL_OFF"></a>

## 378.32 `CONFIG_USBC_PPC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBC_PPC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C 电源路径控制器（PPC）驱动 → USB Type-C 电源路径控制器（usbc-ppc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBC_PPC_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_PPC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBC_PPC_LOG_LEVEL_WRN"></a>

## 378.33 `CONFIG_USBC_PPC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBC_PPC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB-C 电源路径控制器（PPC）驱动 → USB Type-C 电源路径控制器（usbc-ppc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBC_PPC_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_PPC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBC_STACK_LOG_LEVEL_CHOICE"></a>

## 378.34 `CONFIG_USBC_STACK_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB Type-C 协议栈（usbc stack）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USBC_STACK
```

**默认值（Defaults）**

```text
CONFIG_USBC_STACK_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USBC_STACK_LOG_LEVEL_OFF
CONFIG_USBC_STACK_LOG_LEVEL_ERR
CONFIG_USBC_STACK_LOG_LEVEL_WRN
CONFIG_USBC_STACK_LOG_LEVEL_INF
CONFIG_USBC_STACK_LOG_LEVEL_DBG
CONFIG_USBC_STACK_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB-C 协议栈支持（Stack Support）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USBC_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBC_STACK)、[`CONFIG_USBC_STACK_LOG_LEVEL_DEFAULT`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_STACK_LOG_LEVEL_DEFAULT)、[`CONFIG_USBC_STACK_LOG_LEVEL_OFF`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_STACK_LOG_LEVEL_OFF)、[`CONFIG_USBC_STACK_LOG_LEVEL_ERR`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_STACK_LOG_LEVEL_ERR)、[`CONFIG_USBC_STACK_LOG_LEVEL_WRN`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_STACK_LOG_LEVEL_WRN)、[`CONFIG_USBC_STACK_LOG_LEVEL_INF`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_STACK_LOG_LEVEL_INF)、[`CONFIG_USBC_STACK_LOG_LEVEL_DBG`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_STACK_LOG_LEVEL_DBG)。

<a id="CONFIG_USBC_STACK_LOG_LEVEL_DBG"></a>

## 378.35 `CONFIG_USBC_STACK_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBC_STACK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB-C 协议栈支持（Stack Support） → USB Type-C 协议栈（usbc stack）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBC_STACK_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_STACK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBC_STACK_LOG_LEVEL_DEFAULT"></a>

## 378.36 `CONFIG_USBC_STACK_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBC_STACK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB-C 协议栈支持（Stack Support） → USB Type-C 协议栈（usbc stack）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBC_STACK_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_STACK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBC_STACK_LOG_LEVEL_ERR"></a>

## 378.37 `CONFIG_USBC_STACK_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBC_STACK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB-C 协议栈支持（Stack Support） → USB Type-C 协议栈（usbc stack）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBC_STACK_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_STACK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBC_STACK_LOG_LEVEL_INF"></a>

## 378.38 `CONFIG_USBC_STACK_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBC_STACK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB-C 协议栈支持（Stack Support） → USB Type-C 协议栈（usbc stack）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBC_STACK_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_STACK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBC_STACK_LOG_LEVEL_OFF"></a>

## 378.39 `CONFIG_USBC_STACK_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBC_STACK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB-C 协议栈支持（Stack Support） → USB Type-C 协议栈（usbc stack）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBC_STACK_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_STACK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBC_STACK_LOG_LEVEL_WRN"></a>

## 378.40 `CONFIG_USBC_STACK_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBC_STACK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB-C 协议栈支持（Stack Support） → USB Type-C 协议栈（usbc stack）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBC_STACK_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBC_STACK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_BT_HCI_LOG_LEVEL_CHOICE"></a>

## 378.41 `CONFIG_USBD_BT_HCI_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB 设备蓝牙主机控制器接口（usbd bt hci）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USBD_BT_HCI && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
CONFIG_USBD_BT_HCI_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USBD_BT_HCI_LOG_LEVEL_OFF
CONFIG_USBD_BT_HCI_LOG_LEVEL_ERR
CONFIG_USBD_BT_HCI_LOG_LEVEL_WRN
CONFIG_USBD_BT_HCI_LOG_LEVEL_INF
CONFIG_USBD_BT_HCI_LOG_LEVEL_DBG
CONFIG_USBD_BT_HCI_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → 蓝牙 HCI USB 传输层（Transport Layer）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USBD_BT_HCI`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_BT_HCI)、[`CONFIG_USB_DEVICE_STACK_NEXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK_NEXT)、[`CONFIG_USBD_BT_HCI_LOG_LEVEL_DEFAULT`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_BT_HCI_LOG_LEVEL_DEFAULT)、[`CONFIG_USBD_BT_HCI_LOG_LEVEL_OFF`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_BT_HCI_LOG_LEVEL_OFF)、[`CONFIG_USBD_BT_HCI_LOG_LEVEL_ERR`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_BT_HCI_LOG_LEVEL_ERR)、[`CONFIG_USBD_BT_HCI_LOG_LEVEL_WRN`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_BT_HCI_LOG_LEVEL_WRN)、[`CONFIG_USBD_BT_HCI_LOG_LEVEL_INF`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_BT_HCI_LOG_LEVEL_INF)、[`CONFIG_USBD_BT_HCI_LOG_LEVEL_DBG`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_BT_HCI_LOG_LEVEL_DBG)。

<a id="CONFIG_USBD_BT_HCI_LOG_LEVEL_DBG"></a>

## 378.42 `CONFIG_USBD_BT_HCI_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_BT_HCI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → 蓝牙 HCI USB 传输层（Transport Layer） → USB 设备蓝牙主机控制器接口（usbd bt hci）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_BT_HCI_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_BT_HCI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_BT_HCI_LOG_LEVEL_DEFAULT"></a>

## 378.43 `CONFIG_USBD_BT_HCI_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_BT_HCI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → 蓝牙 HCI USB 传输层（Transport Layer） → USB 设备蓝牙主机控制器接口（usbd bt hci）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_BT_HCI_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_BT_HCI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_BT_HCI_LOG_LEVEL_ERR"></a>

## 378.44 `CONFIG_USBD_BT_HCI_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_BT_HCI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → 蓝牙 HCI USB 传输层（Transport Layer） → USB 设备蓝牙主机控制器接口（usbd bt hci）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_BT_HCI_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_BT_HCI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_BT_HCI_LOG_LEVEL_INF"></a>

## 378.45 `CONFIG_USBD_BT_HCI_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_BT_HCI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → 蓝牙 HCI USB 传输层（Transport Layer） → USB 设备蓝牙主机控制器接口（usbd bt hci）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_BT_HCI_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_BT_HCI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_BT_HCI_LOG_LEVEL_OFF"></a>

## 378.46 `CONFIG_USBD_BT_HCI_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_BT_HCI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → 蓝牙 HCI USB 传输层（Transport Layer） → USB 设备蓝牙主机控制器接口（usbd bt hci）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_BT_HCI_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_BT_HCI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_BT_HCI_LOG_LEVEL_WRN"></a>

## 378.47 `CONFIG_USBD_BT_HCI_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_BT_HCI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → 蓝牙 HCI USB 传输层（Transport Layer） → USB 设备蓝牙主机控制器接口（usbd bt hci）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_BT_HCI_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_BT_HCI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_CDC_ACM_LOG_LEVEL_CHOICE"></a>

## 378.48 `CONFIG_USBD_CDC_ACM_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB 设备通信类抽象控制模型（usbd cdc_acm）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USBD_CDC_ACM_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
CONFIG_USBD_CDC_ACM_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USBD_CDC_ACM_LOG_LEVEL_OFF
CONFIG_USBD_CDC_ACM_LOG_LEVEL_ERR
CONFIG_USBD_CDC_ACM_LOG_LEVEL_WRN
CONFIG_USBD_CDC_ACM_LOG_LEVEL_INF
CONFIG_USBD_CDC_ACM_LOG_LEVEL_DBG
CONFIG_USBD_CDC_ACM_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 通信设备类抽象控制模型实现（CDC ACM）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USBD_CDC_ACM_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_CDC_ACM_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK_NEXT)、[`CONFIG_USBD_CDC_ACM_LOG_LEVEL_DEFAULT`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_ACM_LOG_LEVEL_DEFAULT)、[`CONFIG_USBD_CDC_ACM_LOG_LEVEL_OFF`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_ACM_LOG_LEVEL_OFF)、[`CONFIG_USBD_CDC_ACM_LOG_LEVEL_ERR`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_ACM_LOG_LEVEL_ERR)、[`CONFIG_USBD_CDC_ACM_LOG_LEVEL_WRN`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_ACM_LOG_LEVEL_WRN)、[`CONFIG_USBD_CDC_ACM_LOG_LEVEL_INF`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_ACM_LOG_LEVEL_INF)、[`CONFIG_USBD_CDC_ACM_LOG_LEVEL_DBG`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_ACM_LOG_LEVEL_DBG)。

<a id="CONFIG_USBD_CDC_ACM_LOG_LEVEL_DBG"></a>

## 378.49 `CONFIG_USBD_CDC_ACM_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_CDC_ACM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 通信设备类抽象控制模型实现（CDC ACM） → USB 设备通信类抽象控制模型（usbd cdc_acm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_CDC_ACM_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_ACM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_CDC_ACM_LOG_LEVEL_DEFAULT"></a>

## 378.50 `CONFIG_USBD_CDC_ACM_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_CDC_ACM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 通信设备类抽象控制模型实现（CDC ACM） → USB 设备通信类抽象控制模型（usbd cdc_acm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_CDC_ACM_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_ACM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_CDC_ACM_LOG_LEVEL_ERR"></a>

## 378.51 `CONFIG_USBD_CDC_ACM_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_CDC_ACM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 通信设备类抽象控制模型实现（CDC ACM） → USB 设备通信类抽象控制模型（usbd cdc_acm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_CDC_ACM_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_ACM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_CDC_ACM_LOG_LEVEL_INF"></a>

## 378.52 `CONFIG_USBD_CDC_ACM_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_CDC_ACM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 通信设备类抽象控制模型实现（CDC ACM） → USB 设备通信类抽象控制模型（usbd cdc_acm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_CDC_ACM_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_ACM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_CDC_ACM_LOG_LEVEL_OFF"></a>

## 378.53 `CONFIG_USBD_CDC_ACM_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_CDC_ACM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 通信设备类抽象控制模型实现（CDC ACM） → USB 设备通信类抽象控制模型（usbd cdc_acm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_CDC_ACM_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_ACM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_CDC_ACM_LOG_LEVEL_WRN"></a>

## 378.54 `CONFIG_USBD_CDC_ACM_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_CDC_ACM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 通信设备类抽象控制模型实现（CDC ACM） → USB 设备通信类抽象控制模型（usbd cdc_acm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_CDC_ACM_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_ACM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_CDC_ECM_LOG_LEVEL_CHOICE"></a>

## 378.55 `CONFIG_USBD_CDC_ECM_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB 设备通信类以太网控制模型（usbd cdc_ecm）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USBD_CDC_ECM_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
CONFIG_USBD_CDC_ECM_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USBD_CDC_ECM_LOG_LEVEL_OFF
CONFIG_USBD_CDC_ECM_LOG_LEVEL_ERR
CONFIG_USBD_CDC_ECM_LOG_LEVEL_WRN
CONFIG_USBD_CDC_ECM_LOG_LEVEL_INF
CONFIG_USBD_CDC_ECM_LOG_LEVEL_DBG
CONFIG_USBD_CDC_ECM_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 通信设备类以太网控制模型实现（CDC ECM）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USBD_CDC_ECM_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_CDC_ECM_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK_NEXT)、[`CONFIG_USBD_CDC_ECM_LOG_LEVEL_DEFAULT`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_ECM_LOG_LEVEL_DEFAULT)、[`CONFIG_USBD_CDC_ECM_LOG_LEVEL_OFF`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_ECM_LOG_LEVEL_OFF)、[`CONFIG_USBD_CDC_ECM_LOG_LEVEL_ERR`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_ECM_LOG_LEVEL_ERR)、[`CONFIG_USBD_CDC_ECM_LOG_LEVEL_WRN`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_ECM_LOG_LEVEL_WRN)、[`CONFIG_USBD_CDC_ECM_LOG_LEVEL_INF`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_ECM_LOG_LEVEL_INF)、[`CONFIG_USBD_CDC_ECM_LOG_LEVEL_DBG`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_ECM_LOG_LEVEL_DBG)。

<a id="CONFIG_USBD_CDC_ECM_LOG_LEVEL_DBG"></a>

## 378.56 `CONFIG_USBD_CDC_ECM_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_CDC_ECM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 通信设备类以太网控制模型实现（CDC ECM） → USB 设备通信类以太网控制模型（usbd cdc_ecm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_CDC_ECM_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_ECM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_CDC_ECM_LOG_LEVEL_DEFAULT"></a>

## 378.57 `CONFIG_USBD_CDC_ECM_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_CDC_ECM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 通信设备类以太网控制模型实现（CDC ECM） → USB 设备通信类以太网控制模型（usbd cdc_ecm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_CDC_ECM_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_ECM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_CDC_ECM_LOG_LEVEL_ERR"></a>

## 378.58 `CONFIG_USBD_CDC_ECM_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_CDC_ECM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 通信设备类以太网控制模型实现（CDC ECM） → USB 设备通信类以太网控制模型（usbd cdc_ecm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_CDC_ECM_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_ECM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_CDC_ECM_LOG_LEVEL_INF"></a>

## 378.59 `CONFIG_USBD_CDC_ECM_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_CDC_ECM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 通信设备类以太网控制模型实现（CDC ECM） → USB 设备通信类以太网控制模型（usbd cdc_ecm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_CDC_ECM_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_ECM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_CDC_ECM_LOG_LEVEL_OFF"></a>

## 378.60 `CONFIG_USBD_CDC_ECM_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_CDC_ECM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 通信设备类以太网控制模型实现（CDC ECM） → USB 设备通信类以太网控制模型（usbd cdc_ecm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_CDC_ECM_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_ECM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_CDC_ECM_LOG_LEVEL_WRN"></a>

## 378.61 `CONFIG_USBD_CDC_ECM_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_CDC_ECM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 通信设备类以太网控制模型实现（CDC ECM） → USB 设备通信类以太网控制模型（usbd cdc_ecm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_CDC_ECM_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_ECM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_CDC_NCM_LOG_LEVEL_CHOICE"></a>

## 378.62 `CONFIG_USBD_CDC_NCM_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB 设备通信类网络控制模型（usbd cdc_ncm）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USBD_CDC_NCM_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
CONFIG_USBD_CDC_NCM_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USBD_CDC_NCM_LOG_LEVEL_OFF
CONFIG_USBD_CDC_NCM_LOG_LEVEL_ERR
CONFIG_USBD_CDC_NCM_LOG_LEVEL_WRN
CONFIG_USBD_CDC_NCM_LOG_LEVEL_INF
CONFIG_USBD_CDC_NCM_LOG_LEVEL_DBG
CONFIG_USBD_CDC_NCM_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 通信设备类网络控制模型实现（CDC NCM）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USBD_CDC_NCM_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_CDC_NCM_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK_NEXT)、[`CONFIG_USBD_CDC_NCM_LOG_LEVEL_DEFAULT`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_NCM_LOG_LEVEL_DEFAULT)、[`CONFIG_USBD_CDC_NCM_LOG_LEVEL_OFF`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_NCM_LOG_LEVEL_OFF)、[`CONFIG_USBD_CDC_NCM_LOG_LEVEL_ERR`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_NCM_LOG_LEVEL_ERR)、[`CONFIG_USBD_CDC_NCM_LOG_LEVEL_WRN`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_NCM_LOG_LEVEL_WRN)、[`CONFIG_USBD_CDC_NCM_LOG_LEVEL_INF`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_NCM_LOG_LEVEL_INF)、[`CONFIG_USBD_CDC_NCM_LOG_LEVEL_DBG`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_NCM_LOG_LEVEL_DBG)。

<a id="CONFIG_USBD_CDC_NCM_LOG_LEVEL_DBG"></a>

## 378.63 `CONFIG_USBD_CDC_NCM_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_CDC_NCM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 通信设备类网络控制模型实现（CDC NCM） → USB 设备通信类网络控制模型（usbd cdc_ncm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_CDC_NCM_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_NCM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_CDC_NCM_LOG_LEVEL_DEFAULT"></a>

## 378.64 `CONFIG_USBD_CDC_NCM_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_CDC_NCM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 通信设备类网络控制模型实现（CDC NCM） → USB 设备通信类网络控制模型（usbd cdc_ncm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_CDC_NCM_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_NCM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_CDC_NCM_LOG_LEVEL_ERR"></a>

## 378.65 `CONFIG_USBD_CDC_NCM_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_CDC_NCM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 通信设备类网络控制模型实现（CDC NCM） → USB 设备通信类网络控制模型（usbd cdc_ncm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_CDC_NCM_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_NCM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_CDC_NCM_LOG_LEVEL_INF"></a>

## 378.66 `CONFIG_USBD_CDC_NCM_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_CDC_NCM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 通信设备类网络控制模型实现（CDC NCM） → USB 设备通信类网络控制模型（usbd cdc_ncm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_CDC_NCM_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_NCM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_CDC_NCM_LOG_LEVEL_OFF"></a>

## 378.67 `CONFIG_USBD_CDC_NCM_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_CDC_NCM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 通信设备类网络控制模型实现（CDC NCM） → USB 设备通信类网络控制模型（usbd cdc_ncm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_CDC_NCM_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_NCM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_CDC_NCM_LOG_LEVEL_WRN"></a>

## 378.68 `CONFIG_USBD_CDC_NCM_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_CDC_NCM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 通信设备类网络控制模型实现（CDC NCM） → USB 设备通信类网络控制模型（usbd cdc_ncm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_CDC_NCM_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_CDC_NCM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_DFU_LOG_LEVEL_CHOICE"></a>

## 378.69 `CONFIG_USBD_DFU_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB 设备固件更新类（usbd dfu）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USBD_DFU && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
CONFIG_USBD_DFU_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USBD_DFU_LOG_LEVEL_OFF
CONFIG_USBD_DFU_LOG_LEVEL_ERR
CONFIG_USBD_DFU_LOG_LEVEL_WRN
CONFIG_USBD_DFU_LOG_LEVEL_INF
CONFIG_USBD_DFU_LOG_LEVEL_DBG
CONFIG_USBD_DFU_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 设备固件更新类支持（DFU Class）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USBD_DFU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_DFU)、[`CONFIG_USB_DEVICE_STACK_NEXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK_NEXT)、[`CONFIG_USBD_DFU_LOG_LEVEL_DEFAULT`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_DFU_LOG_LEVEL_DEFAULT)、[`CONFIG_USBD_DFU_LOG_LEVEL_OFF`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_DFU_LOG_LEVEL_OFF)、[`CONFIG_USBD_DFU_LOG_LEVEL_ERR`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_DFU_LOG_LEVEL_ERR)、[`CONFIG_USBD_DFU_LOG_LEVEL_WRN`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_DFU_LOG_LEVEL_WRN)、[`CONFIG_USBD_DFU_LOG_LEVEL_INF`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_DFU_LOG_LEVEL_INF)、[`CONFIG_USBD_DFU_LOG_LEVEL_DBG`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_DFU_LOG_LEVEL_DBG)。

<a id="CONFIG_USBD_DFU_LOG_LEVEL_DBG"></a>

## 378.70 `CONFIG_USBD_DFU_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_DFU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 设备固件更新类支持（DFU Class） → USB 设备固件更新类（usbd dfu）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_DFU_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_DFU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_DFU_LOG_LEVEL_DEFAULT"></a>

## 378.71 `CONFIG_USBD_DFU_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_DFU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 设备固件更新类支持（DFU Class） → USB 设备固件更新类（usbd dfu）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_DFU_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_DFU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_DFU_LOG_LEVEL_ERR"></a>

## 378.72 `CONFIG_USBD_DFU_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_DFU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 设备固件更新类支持（DFU Class） → USB 设备固件更新类（usbd dfu）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_DFU_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_DFU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_DFU_LOG_LEVEL_INF"></a>

## 378.73 `CONFIG_USBD_DFU_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_DFU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 设备固件更新类支持（DFU Class） → USB 设备固件更新类（usbd dfu）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_DFU_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_DFU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_DFU_LOG_LEVEL_OFF"></a>

## 378.74 `CONFIG_USBD_DFU_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_DFU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 设备固件更新类支持（DFU Class） → USB 设备固件更新类（usbd dfu）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_DFU_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_DFU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_DFU_LOG_LEVEL_WRN"></a>

## 378.75 `CONFIG_USBD_DFU_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_DFU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 设备固件更新类支持（DFU Class） → USB 设备固件更新类（usbd dfu）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_DFU_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_DFU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_HID_LOG_LEVEL_CHOICE"></a>

## 378.76 `CONFIG_USBD_HID_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB 人机接口设备类（usbd hid）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USBD_HID_SUPPORT && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
CONFIG_USBD_HID_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USBD_HID_LOG_LEVEL_OFF
CONFIG_USBD_HID_LOG_LEVEL_ERR
CONFIG_USBD_HID_LOG_LEVEL_WRN
CONFIG_USBD_HID_LOG_LEVEL_INF
CONFIG_USBD_HID_LOG_LEVEL_DBG
CONFIG_USBD_HID_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 人机接口设备支持（Human Interface Device）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USBD_HID_SUPPORT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_HID_SUPPORT)、[`CONFIG_USB_DEVICE_STACK_NEXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK_NEXT)、[`CONFIG_USBD_HID_LOG_LEVEL_DEFAULT`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_HID_LOG_LEVEL_DEFAULT)、[`CONFIG_USBD_HID_LOG_LEVEL_OFF`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_HID_LOG_LEVEL_OFF)、[`CONFIG_USBD_HID_LOG_LEVEL_ERR`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_HID_LOG_LEVEL_ERR)、[`CONFIG_USBD_HID_LOG_LEVEL_WRN`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_HID_LOG_LEVEL_WRN)、[`CONFIG_USBD_HID_LOG_LEVEL_INF`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_HID_LOG_LEVEL_INF)、[`CONFIG_USBD_HID_LOG_LEVEL_DBG`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_HID_LOG_LEVEL_DBG)。

<a id="CONFIG_USBD_HID_LOG_LEVEL_DBG"></a>

## 378.77 `CONFIG_USBD_HID_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_HID_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 人机接口设备支持（Human Interface Device） → USB 人机接口设备类（usbd hid）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_HID_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_HID_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_HID_LOG_LEVEL_DEFAULT"></a>

## 378.78 `CONFIG_USBD_HID_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_HID_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 人机接口设备支持（Human Interface Device） → USB 人机接口设备类（usbd hid）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_HID_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_HID_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_HID_LOG_LEVEL_ERR"></a>

## 378.79 `CONFIG_USBD_HID_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_HID_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 人机接口设备支持（Human Interface Device） → USB 人机接口设备类（usbd hid）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_HID_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_HID_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_HID_LOG_LEVEL_INF"></a>

## 378.80 `CONFIG_USBD_HID_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_HID_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 人机接口设备支持（Human Interface Device） → USB 人机接口设备类（usbd hid）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_HID_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_HID_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_HID_LOG_LEVEL_OFF"></a>

## 378.81 `CONFIG_USBD_HID_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_HID_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 人机接口设备支持（Human Interface Device） → USB 人机接口设备类（usbd hid）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_HID_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_HID_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_HID_LOG_LEVEL_WRN"></a>

## 378.82 `CONFIG_USBD_HID_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_HID_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 人机接口设备支持（Human Interface Device） → USB 人机接口设备类（usbd hid）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_HID_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_HID_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_LOG_LEVEL_CHOICE"></a>

## 378.83 `CONFIG_USBD_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB 设备（usbd）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
CONFIG_USBD_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USBD_LOG_LEVEL_OFF
CONFIG_USBD_LOG_LEVEL_ERR
CONFIG_USBD_LOG_LEVEL_WRN
CONFIG_USBD_LOG_LEVEL_INF
CONFIG_USBD_LOG_LEVEL_DBG
CONFIG_USBD_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USB_DEVICE_STACK_NEXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK_NEXT)、[`CONFIG_USBD_LOG_LEVEL_DEFAULT`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_LOG_LEVEL_DEFAULT)、[`CONFIG_USBD_LOG_LEVEL_OFF`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_LOG_LEVEL_OFF)、[`CONFIG_USBD_LOG_LEVEL_ERR`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_LOG_LEVEL_ERR)、[`CONFIG_USBD_LOG_LEVEL_WRN`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_LOG_LEVEL_WRN)、[`CONFIG_USBD_LOG_LEVEL_INF`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_LOG_LEVEL_INF)、[`CONFIG_USBD_LOG_LEVEL_DBG`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_LOG_LEVEL_DBG)。

<a id="CONFIG_USBD_LOG_LEVEL_DBG"></a>

## 378.84 `CONFIG_USBD_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 设备（usbd）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_LOG_LEVEL_DEFAULT"></a>

## 378.85 `CONFIG_USBD_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 设备（usbd）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_LOG_LEVEL_ERR"></a>

## 378.86 `CONFIG_USBD_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 设备（usbd）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_LOG_LEVEL_INF"></a>

## 378.87 `CONFIG_USBD_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 设备（usbd）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_LOG_LEVEL_OFF"></a>

## 378.88 `CONFIG_USBD_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 设备（usbd）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_LOG_LEVEL_WRN"></a>

## 378.89 `CONFIG_USBD_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 设备（usbd）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_LOOPBACK_LOG_LEVEL_CHOICE"></a>

## 378.90 `CONFIG_USBD_LOOPBACK_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB 设备回环类（usbd loopback）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USBD_LOOPBACK_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
CONFIG_USBD_LOOPBACK_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USBD_LOOPBACK_LOG_LEVEL_OFF
CONFIG_USBD_LOOPBACK_LOG_LEVEL_ERR
CONFIG_USBD_LOOPBACK_LOG_LEVEL_WRN
CONFIG_USBD_LOOPBACK_LOG_LEVEL_INF
CONFIG_USBD_LOOPBACK_LOG_LEVEL_DBG
CONFIG_USBD_LOOPBACK_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 回环类（Loopback Class）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USBD_LOOPBACK_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_LOOPBACK_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK_NEXT)、[`CONFIG_USBD_LOOPBACK_LOG_LEVEL_DEFAULT`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_LOOPBACK_LOG_LEVEL_DEFAULT)、[`CONFIG_USBD_LOOPBACK_LOG_LEVEL_OFF`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_LOOPBACK_LOG_LEVEL_OFF)、[`CONFIG_USBD_LOOPBACK_LOG_LEVEL_ERR`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_LOOPBACK_LOG_LEVEL_ERR)、[`CONFIG_USBD_LOOPBACK_LOG_LEVEL_WRN`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_LOOPBACK_LOG_LEVEL_WRN)、[`CONFIG_USBD_LOOPBACK_LOG_LEVEL_INF`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_LOOPBACK_LOG_LEVEL_INF)、[`CONFIG_USBD_LOOPBACK_LOG_LEVEL_DBG`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_LOOPBACK_LOG_LEVEL_DBG)。

<a id="CONFIG_USBD_LOOPBACK_LOG_LEVEL_DBG"></a>

## 378.91 `CONFIG_USBD_LOOPBACK_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_LOOPBACK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 回环类（Loopback Class） → USB 设备回环类（usbd loopback）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_LOOPBACK_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_LOOPBACK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_LOOPBACK_LOG_LEVEL_DEFAULT"></a>

## 378.92 `CONFIG_USBD_LOOPBACK_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_LOOPBACK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 回环类（Loopback Class） → USB 设备回环类（usbd loopback）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_LOOPBACK_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_LOOPBACK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_LOOPBACK_LOG_LEVEL_ERR"></a>

## 378.93 `CONFIG_USBD_LOOPBACK_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_LOOPBACK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 回环类（Loopback Class） → USB 设备回环类（usbd loopback）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_LOOPBACK_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_LOOPBACK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_LOOPBACK_LOG_LEVEL_INF"></a>

## 378.94 `CONFIG_USBD_LOOPBACK_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_LOOPBACK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 回环类（Loopback Class） → USB 设备回环类（usbd loopback）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_LOOPBACK_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_LOOPBACK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_LOOPBACK_LOG_LEVEL_OFF"></a>

## 378.95 `CONFIG_USBD_LOOPBACK_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_LOOPBACK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 回环类（Loopback Class） → USB 设备回环类（usbd loopback）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_LOOPBACK_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_LOOPBACK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_LOOPBACK_LOG_LEVEL_WRN"></a>

## 378.96 `CONFIG_USBD_LOOPBACK_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_LOOPBACK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 回环类（Loopback Class） → USB 设备回环类（usbd loopback）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_LOOPBACK_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_LOOPBACK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_MIDI2_LOG_LEVEL_CHOICE"></a>

## 378.97 `CONFIG_USBD_MIDI2_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB 设备 MIDI 2.0 类（usbd midi2）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USBD_MIDI2_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
CONFIG_USBD_MIDI2_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USBD_MIDI2_LOG_LEVEL_OFF
CONFIG_USBD_MIDI2_LOG_LEVEL_ERR
CONFIG_USBD_MIDI2_LOG_LEVEL_WRN
CONFIG_USBD_MIDI2_LOG_LEVEL_INF
CONFIG_USBD_MIDI2_LOG_LEVEL_DBG
CONFIG_USBD_MIDI2_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB MIDI 2.0 类支持【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USBD_MIDI2_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_MIDI2_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK_NEXT)、[`CONFIG_USBD_MIDI2_LOG_LEVEL_DEFAULT`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_MIDI2_LOG_LEVEL_DEFAULT)、[`CONFIG_USBD_MIDI2_LOG_LEVEL_OFF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_MIDI2_LOG_LEVEL_OFF)、[`CONFIG_USBD_MIDI2_LOG_LEVEL_ERR`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_MIDI2_LOG_LEVEL_ERR)、[`CONFIG_USBD_MIDI2_LOG_LEVEL_WRN`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_MIDI2_LOG_LEVEL_WRN)、[`CONFIG_USBD_MIDI2_LOG_LEVEL_INF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_MIDI2_LOG_LEVEL_INF)、[`CONFIG_USBD_MIDI2_LOG_LEVEL_DBG`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_MIDI2_LOG_LEVEL_DBG)。

<a id="CONFIG_USBD_MIDI2_LOG_LEVEL_DBG"></a>

## 378.98 `CONFIG_USBD_MIDI2_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_MIDI2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB MIDI 2.0 类支持【实验性 EXPERIMENTAL】 → USB 设备 MIDI 2.0 类（usbd midi2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_MIDI2_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_MIDI2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_MIDI2_LOG_LEVEL_DEFAULT"></a>

## 378.99 `CONFIG_USBD_MIDI2_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_MIDI2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB MIDI 2.0 类支持【实验性 EXPERIMENTAL】 → USB 设备 MIDI 2.0 类（usbd midi2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_MIDI2_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_MIDI2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_MIDI2_LOG_LEVEL_ERR"></a>

## 378.100 `CONFIG_USBD_MIDI2_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_MIDI2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB MIDI 2.0 类支持【实验性 EXPERIMENTAL】 → USB 设备 MIDI 2.0 类（usbd midi2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_MIDI2_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_MIDI2_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P377_subsys_logging_配置项参考_26.md) · [返回大纲](大纲.md) · [下一章](P379_subsys_logging_配置项参考_28.md)
