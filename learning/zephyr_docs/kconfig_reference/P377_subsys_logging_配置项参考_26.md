---
id: learning.zephyr-docs.kconfig-reference.page-377
title: "`subsys/logging`配置项参考（26/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第377章\_`subsys/logging`配置项参考（26/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_STM32_USB_COMMON_LOG_LEVEL_CHOICE"></a>

## 377.1 `CONFIG_STM32_USB_COMMON_LOG_LEVEL_CHOICE`

**提示（Prompt）**：STM32 USB 公共代码（STM32 USB common code）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_STM32_USB_COMMON && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
CONFIG_STM32_USB_COMMON_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_STM32_USB_COMMON_LOG_LEVEL_OFF
CONFIG_STM32_USB_COMMON_LOG_LEVEL_ERR
CONFIG_STM32_USB_COMMON_LOG_LEVEL_WRN
CONFIG_STM32_USB_COMMON_LOG_LEVEL_INF
CONFIG_STM32_USB_COMMON_LOG_LEVEL_DBG
CONFIG_STM32_USB_COMMON_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 公共功能（USB Common）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_STM32_USB_COMMON`](P179_drivers_usb_配置项参考_1.md#CONFIG_STM32_USB_COMMON)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_STM32_USB_COMMON_LOG_LEVEL_DEFAULT`](P377_subsys_logging_配置项参考_26.md#CONFIG_STM32_USB_COMMON_LOG_LEVEL_DEFAULT)、[`CONFIG_STM32_USB_COMMON_LOG_LEVEL_OFF`](P377_subsys_logging_配置项参考_26.md#CONFIG_STM32_USB_COMMON_LOG_LEVEL_OFF)、[`CONFIG_STM32_USB_COMMON_LOG_LEVEL_ERR`](P377_subsys_logging_配置项参考_26.md#CONFIG_STM32_USB_COMMON_LOG_LEVEL_ERR)、[`CONFIG_STM32_USB_COMMON_LOG_LEVEL_WRN`](P377_subsys_logging_配置项参考_26.md#CONFIG_STM32_USB_COMMON_LOG_LEVEL_WRN)、[`CONFIG_STM32_USB_COMMON_LOG_LEVEL_INF`](P377_subsys_logging_配置项参考_26.md#CONFIG_STM32_USB_COMMON_LOG_LEVEL_INF)、[`CONFIG_STM32_USB_COMMON_LOG_LEVEL_DBG`](P377_subsys_logging_配置项参考_26.md#CONFIG_STM32_USB_COMMON_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32_USB_COMMON_LOG_LEVEL_DBG"></a>

## 377.2 `CONFIG_STM32_USB_COMMON_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STM32_USB_COMMON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 公共功能（USB Common） → STM32 USB 公共代码（STM32 USB common code）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STM32_USB_COMMON_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_STM32_USB_COMMON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STM32_USB_COMMON_LOG_LEVEL_DEFAULT"></a>

## 377.3 `CONFIG_STM32_USB_COMMON_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STM32_USB_COMMON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 公共功能（USB Common） → STM32 USB 公共代码（STM32 USB common code）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STM32_USB_COMMON_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_STM32_USB_COMMON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STM32_USB_COMMON_LOG_LEVEL_ERR"></a>

## 377.4 `CONFIG_STM32_USB_COMMON_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STM32_USB_COMMON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 公共功能（USB Common） → STM32 USB 公共代码（STM32 USB common code）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STM32_USB_COMMON_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_STM32_USB_COMMON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STM32_USB_COMMON_LOG_LEVEL_INF"></a>

## 377.5 `CONFIG_STM32_USB_COMMON_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STM32_USB_COMMON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 公共功能（USB Common） → STM32 USB 公共代码（STM32 USB common code）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STM32_USB_COMMON_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_STM32_USB_COMMON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STM32_USB_COMMON_LOG_LEVEL_OFF"></a>

## 377.6 `CONFIG_STM32_USB_COMMON_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STM32_USB_COMMON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 公共功能（USB Common） → STM32 USB 公共代码（STM32 USB common code）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STM32_USB_COMMON_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_STM32_USB_COMMON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STM32_USB_COMMON_LOG_LEVEL_WRN"></a>

## 377.7 `CONFIG_STM32_USB_COMMON_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STM32_USB_COMMON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 公共功能（USB Common） → STM32 USB 公共代码（STM32 USB common code）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STM32_USB_COMMON_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_STM32_USB_COMMON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STM32_XSPIM_LOG_LEVEL_CHOICE"></a>

## 377.8 `CONFIG_STM32_XSPIM_LOG_LEVEL_CHOICE`

**提示（Prompt）**：STM32 XPSIM 接口管理器（stm32_xpsim）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_STM32_XSPIM && CONFIG_SOC_FAMILY_STM32
```

**默认值（Defaults）**

```text
CONFIG_STM32_XSPIM_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_STM32_XSPIM_LOG_LEVEL_OFF
CONFIG_STM32_XSPIM_LOG_LEVEL_ERR
CONFIG_STM32_XSPIM_LOG_LEVEL_WRN
CONFIG_STM32_XSPIM_LOG_LEVEL_INF
CONFIG_STM32_XSPIM_LOG_LEVEL_DBG
CONFIG_STM32_XSPIM_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → STM32 XSPI 管理器（Manager）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_STM32_XSPIM`](P311_soc_st_配置项参考.md#CONFIG_STM32_XSPIM)、[`CONFIG_SOC_FAMILY_STM32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_STM32)、[`CONFIG_STM32_XSPIM_LOG_LEVEL_DEFAULT`](P377_subsys_logging_配置项参考_26.md#CONFIG_STM32_XSPIM_LOG_LEVEL_DEFAULT)、[`CONFIG_STM32_XSPIM_LOG_LEVEL_OFF`](P377_subsys_logging_配置项参考_26.md#CONFIG_STM32_XSPIM_LOG_LEVEL_OFF)、[`CONFIG_STM32_XSPIM_LOG_LEVEL_ERR`](P377_subsys_logging_配置项参考_26.md#CONFIG_STM32_XSPIM_LOG_LEVEL_ERR)、[`CONFIG_STM32_XSPIM_LOG_LEVEL_WRN`](P377_subsys_logging_配置项参考_26.md#CONFIG_STM32_XSPIM_LOG_LEVEL_WRN)、[`CONFIG_STM32_XSPIM_LOG_LEVEL_INF`](P377_subsys_logging_配置项参考_26.md#CONFIG_STM32_XSPIM_LOG_LEVEL_INF)、[`CONFIG_STM32_XSPIM_LOG_LEVEL_DBG`](P377_subsys_logging_配置项参考_26.md#CONFIG_STM32_XSPIM_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_STM32`。

<a id="CONFIG_STM32_XSPIM_LOG_LEVEL_DBG"></a>

## 377.9 `CONFIG_STM32_XSPIM_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STM32_XSPIM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → STM32 XSPI 管理器（Manager） → STM32 XPSIM 接口管理器（stm32_xpsim）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STM32_XSPIM_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_STM32_XSPIM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STM32_XSPIM_LOG_LEVEL_DEFAULT"></a>

## 377.10 `CONFIG_STM32_XSPIM_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STM32_XSPIM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → STM32 XSPI 管理器（Manager） → STM32 XPSIM 接口管理器（stm32_xpsim）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STM32_XSPIM_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_STM32_XSPIM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STM32_XSPIM_LOG_LEVEL_ERR"></a>

## 377.11 `CONFIG_STM32_XSPIM_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STM32_XSPIM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → STM32 XSPI 管理器（Manager） → STM32 XPSIM 接口管理器（stm32_xpsim）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STM32_XSPIM_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_STM32_XSPIM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STM32_XSPIM_LOG_LEVEL_INF"></a>

## 377.12 `CONFIG_STM32_XSPIM_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STM32_XSPIM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → STM32 XSPI 管理器（Manager） → STM32 XPSIM 接口管理器（stm32_xpsim）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STM32_XSPIM_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_STM32_XSPIM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STM32_XSPIM_LOG_LEVEL_OFF"></a>

## 377.13 `CONFIG_STM32_XSPIM_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STM32_XSPIM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → STM32 XSPI 管理器（Manager） → STM32 XPSIM 接口管理器（stm32_xpsim）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STM32_XSPIM_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_STM32_XSPIM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STM32_XSPIM_LOG_LEVEL_WRN"></a>

## 377.14 `CONFIG_STM32_XSPIM_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STM32_XSPIM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → STM32 XSPI 管理器（Manager） → STM32 XPSIM 接口管理器（stm32_xpsim）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STM32_XSPIM_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_STM32_XSPIM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STREAM_FLASH_LOG_LEVEL_CHOICE"></a>

## 377.15 `CONFIG_STREAM_FLASH_LOG_LEVEL_CHOICE`

**提示（Prompt）**：闪存流写入（stream flash）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_STREAM_FLASH
```

**默认值（Defaults）**

```text
CONFIG_STREAM_FLASH_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_STREAM_FLASH_LOG_LEVEL_OFF
CONFIG_STREAM_FLASH_LOG_LEVEL_ERR
CONFIG_STREAM_FLASH_LOG_LEVEL_WRN
CONFIG_STREAM_FLASH_LOG_LEVEL_INF
CONFIG_STREAM_FLASH_LOG_LEVEL_DBG
CONFIG_STREAM_FLASH_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 存储（Storage） → 流式写入闪存（Stream to flash）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_STREAM_FLASH`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_STREAM_FLASH)、[`CONFIG_STREAM_FLASH_LOG_LEVEL_DEFAULT`](P377_subsys_logging_配置项参考_26.md#CONFIG_STREAM_FLASH_LOG_LEVEL_DEFAULT)、[`CONFIG_STREAM_FLASH_LOG_LEVEL_OFF`](P377_subsys_logging_配置项参考_26.md#CONFIG_STREAM_FLASH_LOG_LEVEL_OFF)、[`CONFIG_STREAM_FLASH_LOG_LEVEL_ERR`](P377_subsys_logging_配置项参考_26.md#CONFIG_STREAM_FLASH_LOG_LEVEL_ERR)、[`CONFIG_STREAM_FLASH_LOG_LEVEL_WRN`](P377_subsys_logging_配置项参考_26.md#CONFIG_STREAM_FLASH_LOG_LEVEL_WRN)、[`CONFIG_STREAM_FLASH_LOG_LEVEL_INF`](P377_subsys_logging_配置项参考_26.md#CONFIG_STREAM_FLASH_LOG_LEVEL_INF)、[`CONFIG_STREAM_FLASH_LOG_LEVEL_DBG`](P377_subsys_logging_配置项参考_26.md#CONFIG_STREAM_FLASH_LOG_LEVEL_DBG)。

<a id="CONFIG_STREAM_FLASH_LOG_LEVEL_DBG"></a>

## 377.16 `CONFIG_STREAM_FLASH_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STREAM_FLASH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 存储（Storage） → 流式写入闪存（Stream to flash） → 闪存流写入（stream flash）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STREAM_FLASH_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_STREAM_FLASH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STREAM_FLASH_LOG_LEVEL_DEFAULT"></a>

## 377.17 `CONFIG_STREAM_FLASH_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STREAM_FLASH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 存储（Storage） → 流式写入闪存（Stream to flash） → 闪存流写入（stream flash）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STREAM_FLASH_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_STREAM_FLASH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STREAM_FLASH_LOG_LEVEL_ERR"></a>

## 377.18 `CONFIG_STREAM_FLASH_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STREAM_FLASH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 存储（Storage） → 流式写入闪存（Stream to flash） → 闪存流写入（stream flash）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STREAM_FLASH_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_STREAM_FLASH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STREAM_FLASH_LOG_LEVEL_INF"></a>

## 377.19 `CONFIG_STREAM_FLASH_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STREAM_FLASH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 存储（Storage） → 流式写入闪存（Stream to flash） → 闪存流写入（stream flash）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STREAM_FLASH_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_STREAM_FLASH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STREAM_FLASH_LOG_LEVEL_OFF"></a>

## 377.20 `CONFIG_STREAM_FLASH_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STREAM_FLASH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 存储（Storage） → 流式写入闪存（Stream to flash） → 闪存流写入（stream flash）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STREAM_FLASH_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_STREAM_FLASH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_STREAM_FLASH_LOG_LEVEL_WRN"></a>

## 377.21 `CONFIG_STREAM_FLASH_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_STREAM_FLASH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 存储（Storage） → 流式写入闪存（Stream to flash） → 闪存流写入（stream flash）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_STREAM_FLASH_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_STREAM_FLASH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SYNC_RTC_LOG_LEVEL_CHOICE"></a>

## 377.22 `CONFIG_SYNC_RTC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：同步实时时钟（Synchronized RTC）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_NRF53_SYNC_RTC && CONFIG_SOC_SERIES_NRF53 && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
CONFIG_SYNC_RTC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_SYNC_RTC_LOG_LEVEL_OFF
CONFIG_SYNC_RTC_LOG_LEVEL_ERR
CONFIG_SYNC_RTC_LOG_LEVEL_WRN
CONFIG_SYNC_RTC_LOG_LEVEL_INF
CONFIG_SYNC_RTC_LOG_LEVEL_DBG
CONFIG_SYNC_RTC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 实时时钟同步（RTC clock synchronization）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_NRF53_SYNC_RTC`](P289_soc_nordic_配置项参考_1.md#CONFIG_NRF53_SYNC_RTC)、[`CONFIG_SOC_SERIES_NRF53`](P291_soc_nordic_配置项参考_3.md#CONFIG_SOC_SERIES_NRF53)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_SYNC_RTC_LOG_LEVEL_DEFAULT`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYNC_RTC_LOG_LEVEL_DEFAULT)、[`CONFIG_SYNC_RTC_LOG_LEVEL_OFF`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYNC_RTC_LOG_LEVEL_OFF)、[`CONFIG_SYNC_RTC_LOG_LEVEL_ERR`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYNC_RTC_LOG_LEVEL_ERR)、[`CONFIG_SYNC_RTC_LOG_LEVEL_WRN`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYNC_RTC_LOG_LEVEL_WRN)、[`CONFIG_SYNC_RTC_LOG_LEVEL_INF`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYNC_RTC_LOG_LEVEL_INF)、[`CONFIG_SYNC_RTC_LOG_LEVEL_DBG`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYNC_RTC_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_SYNC_RTC_LOG_LEVEL_DBG"></a>

## 377.23 `CONFIG_SYNC_RTC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SYNC_RTC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 实时时钟同步（RTC clock synchronization） → 同步实时时钟（Synchronized RTC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SYNC_RTC_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYNC_RTC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SYNC_RTC_LOG_LEVEL_DEFAULT"></a>

## 377.24 `CONFIG_SYNC_RTC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SYNC_RTC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 实时时钟同步（RTC clock synchronization） → 同步实时时钟（Synchronized RTC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SYNC_RTC_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYNC_RTC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SYNC_RTC_LOG_LEVEL_ERR"></a>

## 377.25 `CONFIG_SYNC_RTC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SYNC_RTC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 实时时钟同步（RTC clock synchronization） → 同步实时时钟（Synchronized RTC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SYNC_RTC_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYNC_RTC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SYNC_RTC_LOG_LEVEL_INF"></a>

## 377.26 `CONFIG_SYNC_RTC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SYNC_RTC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 实时时钟同步（RTC clock synchronization） → 同步实时时钟（Synchronized RTC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SYNC_RTC_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYNC_RTC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SYNC_RTC_LOG_LEVEL_OFF"></a>

## 377.27 `CONFIG_SYNC_RTC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SYNC_RTC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 实时时钟同步（RTC clock synchronization） → 同步实时时钟（Synchronized RTC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SYNC_RTC_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYNC_RTC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SYNC_RTC_LOG_LEVEL_WRN"></a>

## 377.28 `CONFIG_SYNC_RTC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SYNC_RTC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 实时时钟同步（RTC clock synchronization） → 同步实时时钟（Synchronized RTC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SYNC_RTC_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYNC_RTC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SYSCON_LOG_LEVEL_CHOICE"></a>

## 377.29 `CONFIG_SYSCON_LOG_LEVEL_CHOICE`

**提示（Prompt）**：系统控制器（syscon）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_SYSCON
```

**默认值（Defaults）**

```text
CONFIG_SYSCON_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_SYSCON_LOG_LEVEL_OFF
CONFIG_SYSCON_LOG_LEVEL_ERR
CONFIG_SYSCON_LOG_LEVEL_WRN
CONFIG_SYSCON_LOG_LEVEL_INF
CONFIG_SYSCON_LOG_LEVEL_DBG
CONFIG_SYSCON_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统控制器（System Controller，SYSCON）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SYSCON`](P175_drivers_syscon_配置项参考.md#CONFIG_SYSCON)、[`CONFIG_SYSCON_LOG_LEVEL_DEFAULT`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYSCON_LOG_LEVEL_DEFAULT)、[`CONFIG_SYSCON_LOG_LEVEL_OFF`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYSCON_LOG_LEVEL_OFF)、[`CONFIG_SYSCON_LOG_LEVEL_ERR`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYSCON_LOG_LEVEL_ERR)、[`CONFIG_SYSCON_LOG_LEVEL_WRN`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYSCON_LOG_LEVEL_WRN)、[`CONFIG_SYSCON_LOG_LEVEL_INF`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYSCON_LOG_LEVEL_INF)、[`CONFIG_SYSCON_LOG_LEVEL_DBG`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYSCON_LOG_LEVEL_DBG)。

<a id="CONFIG_SYSCON_LOG_LEVEL_DBG"></a>

## 377.30 `CONFIG_SYSCON_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SYSCON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统控制器（System Controller，SYSCON）驱动 → 系统控制器（syscon）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SYSCON_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYSCON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SYSCON_LOG_LEVEL_DEFAULT"></a>

## 377.31 `CONFIG_SYSCON_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SYSCON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统控制器（System Controller，SYSCON）驱动 → 系统控制器（syscon）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SYSCON_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYSCON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SYSCON_LOG_LEVEL_ERR"></a>

## 377.32 `CONFIG_SYSCON_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SYSCON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统控制器（System Controller，SYSCON）驱动 → 系统控制器（syscon）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SYSCON_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYSCON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SYSCON_LOG_LEVEL_INF"></a>

## 377.33 `CONFIG_SYSCON_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SYSCON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统控制器（System Controller，SYSCON）驱动 → 系统控制器（syscon）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SYSCON_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYSCON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SYSCON_LOG_LEVEL_OFF"></a>

## 377.34 `CONFIG_SYSCON_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SYSCON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统控制器（System Controller，SYSCON）驱动 → 系统控制器（syscon）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SYSCON_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYSCON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SYSCON_LOG_LEVEL_WRN"></a>

## 377.35 `CONFIG_SYSCON_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SYSCON_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 系统控制器（System Controller，SYSCON）驱动 → 系统控制器（syscon）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SYSCON_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYSCON_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SYS_HEAP_LOG_LEVEL_CHOICE"></a>

## 377.36 `CONFIG_SYS_HEAP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：系统堆（sys_heap）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG
```

**默认值（Defaults）**

```text
CONFIG_SYS_HEAP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_SYS_HEAP_LOG_LEVEL_OFF
CONFIG_SYS_HEAP_LOG_LEVEL_ERR
CONFIG_SYS_HEAP_LOG_LEVEL_WRN
CONFIG_SYS_HEAP_LOG_LEVEL_INF
CONFIG_SYS_HEAP_LOG_LEVEL_DBG
CONFIG_SYS_HEAP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 堆与内存分配（Heap and Memory Allocation）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SYS_HEAP_LOG_LEVEL_DEFAULT`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYS_HEAP_LOG_LEVEL_DEFAULT)、[`CONFIG_SYS_HEAP_LOG_LEVEL_OFF`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYS_HEAP_LOG_LEVEL_OFF)、[`CONFIG_SYS_HEAP_LOG_LEVEL_ERR`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYS_HEAP_LOG_LEVEL_ERR)、[`CONFIG_SYS_HEAP_LOG_LEVEL_WRN`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYS_HEAP_LOG_LEVEL_WRN)、[`CONFIG_SYS_HEAP_LOG_LEVEL_INF`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYS_HEAP_LOG_LEVEL_INF)、[`CONFIG_SYS_HEAP_LOG_LEVEL_DBG`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYS_HEAP_LOG_LEVEL_DBG)。

<a id="CONFIG_SYS_HEAP_LOG_LEVEL_DBG"></a>

## 377.37 `CONFIG_SYS_HEAP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SYS_HEAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 堆与内存分配（Heap and Memory Allocation） → 系统堆（sys_heap）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SYS_HEAP_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYS_HEAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SYS_HEAP_LOG_LEVEL_DEFAULT"></a>

## 377.38 `CONFIG_SYS_HEAP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SYS_HEAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 堆与内存分配（Heap and Memory Allocation） → 系统堆（sys_heap）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SYS_HEAP_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYS_HEAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SYS_HEAP_LOG_LEVEL_ERR"></a>

## 377.39 `CONFIG_SYS_HEAP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SYS_HEAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 堆与内存分配（Heap and Memory Allocation） → 系统堆（sys_heap）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SYS_HEAP_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYS_HEAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SYS_HEAP_LOG_LEVEL_INF"></a>

## 377.40 `CONFIG_SYS_HEAP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SYS_HEAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 堆与内存分配（Heap and Memory Allocation） → 系统堆（sys_heap）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SYS_HEAP_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYS_HEAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SYS_HEAP_LOG_LEVEL_OFF"></a>

## 377.41 `CONFIG_SYS_HEAP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SYS_HEAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 堆与内存分配（Heap and Memory Allocation） → 系统堆（sys_heap）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SYS_HEAP_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYS_HEAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_SYS_HEAP_LOG_LEVEL_WRN"></a>

## 377.42 `CONFIG_SYS_HEAP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_SYS_HEAP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 堆与内存分配（Heap and Memory Allocation） → 系统堆（sys_heap）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_SYS_HEAP_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_SYS_HEAP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_THREAD_ANALYZER_LOG_LEVEL_CHOICE"></a>

## 377.43 `CONFIG_THREAD_ANALYZER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：线程分析器（thread analyzer）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_THREAD_ANALYZER
```

**默认值（Defaults）**

```text
CONFIG_THREAD_ANALYZER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_THREAD_ANALYZER_LOG_LEVEL_OFF
CONFIG_THREAD_ANALYZER_LOG_LEVEL_ERR
CONFIG_THREAD_ANALYZER_LOG_LEVEL_WRN
CONFIG_THREAD_ANALYZER_LOG_LEVEL_INF
CONFIG_THREAD_ANALYZER_LOG_LEVEL_DBG
CONFIG_THREAD_ANALYZER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 系统监控选项（System Monitoring Options） → 线程分析器（Thread Analyzer）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_THREAD_ANALYZER`](P338_subsys_debug_配置项参考.md#CONFIG_THREAD_ANALYZER)、[`CONFIG_THREAD_ANALYZER_LOG_LEVEL_DEFAULT`](P377_subsys_logging_配置项参考_26.md#CONFIG_THREAD_ANALYZER_LOG_LEVEL_DEFAULT)、[`CONFIG_THREAD_ANALYZER_LOG_LEVEL_OFF`](P377_subsys_logging_配置项参考_26.md#CONFIG_THREAD_ANALYZER_LOG_LEVEL_OFF)、[`CONFIG_THREAD_ANALYZER_LOG_LEVEL_ERR`](P377_subsys_logging_配置项参考_26.md#CONFIG_THREAD_ANALYZER_LOG_LEVEL_ERR)、[`CONFIG_THREAD_ANALYZER_LOG_LEVEL_WRN`](P377_subsys_logging_配置项参考_26.md#CONFIG_THREAD_ANALYZER_LOG_LEVEL_WRN)、[`CONFIG_THREAD_ANALYZER_LOG_LEVEL_INF`](P377_subsys_logging_配置项参考_26.md#CONFIG_THREAD_ANALYZER_LOG_LEVEL_INF)、[`CONFIG_THREAD_ANALYZER_LOG_LEVEL_DBG`](P377_subsys_logging_配置项参考_26.md#CONFIG_THREAD_ANALYZER_LOG_LEVEL_DBG)。

<a id="CONFIG_THREAD_ANALYZER_LOG_LEVEL_DBG"></a>

## 377.44 `CONFIG_THREAD_ANALYZER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_THREAD_ANALYZER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 系统监控选项（System Monitoring Options） → 线程分析器（Thread Analyzer） → 线程分析器（thread analyzer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_THREAD_ANALYZER_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_THREAD_ANALYZER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_THREAD_ANALYZER_LOG_LEVEL_DEFAULT"></a>

## 377.45 `CONFIG_THREAD_ANALYZER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_THREAD_ANALYZER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 系统监控选项（System Monitoring Options） → 线程分析器（Thread Analyzer） → 线程分析器（thread analyzer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_THREAD_ANALYZER_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_THREAD_ANALYZER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_THREAD_ANALYZER_LOG_LEVEL_ERR"></a>

## 377.46 `CONFIG_THREAD_ANALYZER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_THREAD_ANALYZER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 系统监控选项（System Monitoring Options） → 线程分析器（Thread Analyzer） → 线程分析器（thread analyzer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_THREAD_ANALYZER_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_THREAD_ANALYZER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_THREAD_ANALYZER_LOG_LEVEL_INF"></a>

## 377.47 `CONFIG_THREAD_ANALYZER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_THREAD_ANALYZER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 系统监控选项（System Monitoring Options） → 线程分析器（Thread Analyzer） → 线程分析器（thread analyzer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_THREAD_ANALYZER_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_THREAD_ANALYZER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_THREAD_ANALYZER_LOG_LEVEL_OFF"></a>

## 377.48 `CONFIG_THREAD_ANALYZER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_THREAD_ANALYZER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 系统监控选项（System Monitoring Options） → 线程分析器（Thread Analyzer） → 线程分析器（thread analyzer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_THREAD_ANALYZER_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_THREAD_ANALYZER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_THREAD_ANALYZER_LOG_LEVEL_WRN"></a>

## 377.49 `CONFIG_THREAD_ANALYZER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_THREAD_ANALYZER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 系统监控选项（System Monitoring Options） → 线程分析器（Thread Analyzer） → 线程分析器（thread analyzer）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_THREAD_ANALYZER_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_THREAD_ANALYZER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_CHOICE"></a>

## 377.50 `CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_CHOICE`

**提示（Prompt）**：时间感知通用输入输出（timeaware_gpio）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_TIMEAWARE_GPIO
```

**默认值（Defaults）**

```text
CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_OFF
CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_ERR
CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_WRN
CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_INF
CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_DBG
CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时间感知 GPIO（Time-aware GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_TIMEAWARE_GPIO`](P177_drivers_timeaware_gpio_配置项参考.md#CONFIG_TIMEAWARE_GPIO)、[`CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_DEFAULT`](P377_subsys_logging_配置项参考_26.md#CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_DEFAULT)、[`CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_OFF`](P377_subsys_logging_配置项参考_26.md#CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_OFF)、[`CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_ERR`](P377_subsys_logging_配置项参考_26.md#CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_ERR)、[`CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_WRN`](P377_subsys_logging_配置项参考_26.md#CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_WRN)、[`CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_INF`](P377_subsys_logging_配置项参考_26.md#CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_INF)、[`CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_DBG`](P377_subsys_logging_配置项参考_26.md#CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_DBG)。

<a id="CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_DBG"></a>

## 377.51 `CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时间感知 GPIO（Time-aware GPIO）驱动 → 时间感知通用输入输出（timeaware_gpio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_DEFAULT"></a>

## 377.52 `CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时间感知 GPIO（Time-aware GPIO）驱动 → 时间感知通用输入输出（timeaware_gpio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_ERR"></a>

## 377.53 `CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时间感知 GPIO（Time-aware GPIO）驱动 → 时间感知通用输入输出（timeaware_gpio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_INF"></a>

## 377.54 `CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时间感知 GPIO（Time-aware GPIO）驱动 → 时间感知通用输入输出（timeaware_gpio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_OFF"></a>

## 377.55 `CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时间感知 GPIO（Time-aware GPIO）驱动 → 时间感知通用输入输出（timeaware_gpio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_WRN"></a>

## 377.56 `CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 时间感知 GPIO（Time-aware GPIO）驱动 → 时间感知通用输入输出（timeaware_gpio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TIMEAWARE_GPIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TIMER_LOG_LEVEL_CHOICE"></a>

## 377.57 `CONFIG_TIMER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：POSIX 定时器（POSIX Timers）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_POSIX_TIMERS && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
CONFIG_TIMER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_TIMER_LOG_LEVEL_OFF
CONFIG_TIMER_LOG_LEVEL_ERR
CONFIG_TIMER_LOG_LEVEL_WRN
CONFIG_TIMER_LOG_LEVEL_INF
CONFIG_TIMER_LOG_LEVEL_DBG
CONFIG_TIMER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 定时器、时钟及休眠函数（timers, clocks, and sleep functions）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_POSIX_TIMERS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_TIMERS)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_TIMER_LOG_LEVEL_DEFAULT`](P377_subsys_logging_配置项参考_26.md#CONFIG_TIMER_LOG_LEVEL_DEFAULT)、[`CONFIG_TIMER_LOG_LEVEL_OFF`](P377_subsys_logging_配置项参考_26.md#CONFIG_TIMER_LOG_LEVEL_OFF)、[`CONFIG_TIMER_LOG_LEVEL_ERR`](P377_subsys_logging_配置项参考_26.md#CONFIG_TIMER_LOG_LEVEL_ERR)、[`CONFIG_TIMER_LOG_LEVEL_WRN`](P377_subsys_logging_配置项参考_26.md#CONFIG_TIMER_LOG_LEVEL_WRN)、[`CONFIG_TIMER_LOG_LEVEL_INF`](P377_subsys_logging_配置项参考_26.md#CONFIG_TIMER_LOG_LEVEL_INF)、[`CONFIG_TIMER_LOG_LEVEL_DBG`](P377_subsys_logging_配置项参考_26.md#CONFIG_TIMER_LOG_LEVEL_DBG)。

<a id="CONFIG_TIMER_LOG_LEVEL_DBG"></a>

## 377.58 `CONFIG_TIMER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TIMER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 定时器、时钟及休眠函数（timers, clocks, and sleep functions） → POSIX 定时器（POSIX Timers）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TIMER_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TIMER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TIMER_LOG_LEVEL_DEFAULT"></a>

## 377.59 `CONFIG_TIMER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TIMER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 定时器、时钟及休眠函数（timers, clocks, and sleep functions） → POSIX 定时器（POSIX Timers）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TIMER_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TIMER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TIMER_LOG_LEVEL_ERR"></a>

## 377.60 `CONFIG_TIMER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TIMER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 定时器、时钟及休眠函数（timers, clocks, and sleep functions） → POSIX 定时器（POSIX Timers）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TIMER_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TIMER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TIMER_LOG_LEVEL_INF"></a>

## 377.61 `CONFIG_TIMER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TIMER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 定时器、时钟及休眠函数（timers, clocks, and sleep functions） → POSIX 定时器（POSIX Timers）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TIMER_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TIMER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TIMER_LOG_LEVEL_OFF"></a>

## 377.62 `CONFIG_TIMER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TIMER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 定时器、时钟及休眠函数（timers, clocks, and sleep functions） → POSIX 定时器（POSIX Timers）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TIMER_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TIMER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TIMER_LOG_LEVEL_WRN"></a>

## 377.63 `CONFIG_TIMER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TIMER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → POSIX 定时器、时钟及休眠函数（timers, clocks, and sleep functions） → POSIX 定时器（POSIX Timers）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TIMER_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TIMER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TI_TDP2004_LOG_LEVEL_CHOICE"></a>

## 377.64 `CONFIG_TI_TDP2004_LOG_LEVEL_CHOICE`

**提示（Prompt）**：TI TDP2004 DisplayPort 与 HDMI 线性重驱动器（TI TDP2004 DisplayPort and HDMI linear redriver）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_TI_TDP2004
```

**默认值（Defaults）**

```text
CONFIG_TI_TDP2004_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_TI_TDP2004_LOG_LEVEL_OFF
CONFIG_TI_TDP2004_LOG_LEVEL_ERR
CONFIG_TI_TDP2004_LOG_LEVEL_WRN
CONFIG_TI_TDP2004_LOG_LEVEL_INF
CONFIG_TI_TDP2004_LOG_LEVEL_DBG
CONFIG_TI_TDP2004_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → TDP2004 四通道 20 Gbps DisplayPort 2.1 和 12 Gbps HDMI 2.1 线性重驱动器（Linear Redriver）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_TI_TDP2004`](P123_drivers_misc_配置项参考.md#CONFIG_TI_TDP2004)、[`CONFIG_TI_TDP2004_LOG_LEVEL_DEFAULT`](P377_subsys_logging_配置项参考_26.md#CONFIG_TI_TDP2004_LOG_LEVEL_DEFAULT)、[`CONFIG_TI_TDP2004_LOG_LEVEL_OFF`](P377_subsys_logging_配置项参考_26.md#CONFIG_TI_TDP2004_LOG_LEVEL_OFF)、[`CONFIG_TI_TDP2004_LOG_LEVEL_ERR`](P377_subsys_logging_配置项参考_26.md#CONFIG_TI_TDP2004_LOG_LEVEL_ERR)、[`CONFIG_TI_TDP2004_LOG_LEVEL_WRN`](P377_subsys_logging_配置项参考_26.md#CONFIG_TI_TDP2004_LOG_LEVEL_WRN)、[`CONFIG_TI_TDP2004_LOG_LEVEL_INF`](P377_subsys_logging_配置项参考_26.md#CONFIG_TI_TDP2004_LOG_LEVEL_INF)、[`CONFIG_TI_TDP2004_LOG_LEVEL_DBG`](P377_subsys_logging_配置项参考_26.md#CONFIG_TI_TDP2004_LOG_LEVEL_DBG)。

<a id="CONFIG_TI_TDP2004_LOG_LEVEL_DBG"></a>

## 377.65 `CONFIG_TI_TDP2004_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TI_TDP2004_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → TDP2004 四通道 20 Gbps DisplayPort 2.1 和 12 Gbps HDMI 2.1 线性重驱动器（Linear Redriver） → TI TDP2004 DisplayPort 与 HDMI 线性重驱动器（TI TDP2004 DisplayPort and HDMI linear redriver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TI_TDP2004_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TI_TDP2004_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TI_TDP2004_LOG_LEVEL_DEFAULT"></a>

## 377.66 `CONFIG_TI_TDP2004_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TI_TDP2004_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → TDP2004 四通道 20 Gbps DisplayPort 2.1 和 12 Gbps HDMI 2.1 线性重驱动器（Linear Redriver） → TI TDP2004 DisplayPort 与 HDMI 线性重驱动器（TI TDP2004 DisplayPort and HDMI linear redriver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TI_TDP2004_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TI_TDP2004_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TI_TDP2004_LOG_LEVEL_ERR"></a>

## 377.67 `CONFIG_TI_TDP2004_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TI_TDP2004_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → TDP2004 四通道 20 Gbps DisplayPort 2.1 和 12 Gbps HDMI 2.1 线性重驱动器（Linear Redriver） → TI TDP2004 DisplayPort 与 HDMI 线性重驱动器（TI TDP2004 DisplayPort and HDMI linear redriver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TI_TDP2004_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TI_TDP2004_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TI_TDP2004_LOG_LEVEL_INF"></a>

## 377.68 `CONFIG_TI_TDP2004_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TI_TDP2004_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → TDP2004 四通道 20 Gbps DisplayPort 2.1 和 12 Gbps HDMI 2.1 线性重驱动器（Linear Redriver） → TI TDP2004 DisplayPort 与 HDMI 线性重驱动器（TI TDP2004 DisplayPort and HDMI linear redriver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TI_TDP2004_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TI_TDP2004_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TI_TDP2004_LOG_LEVEL_OFF"></a>

## 377.69 `CONFIG_TI_TDP2004_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TI_TDP2004_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → TDP2004 四通道 20 Gbps DisplayPort 2.1 和 12 Gbps HDMI 2.1 线性重驱动器（Linear Redriver） → TI TDP2004 DisplayPort 与 HDMI 线性重驱动器（TI TDP2004 DisplayPort and HDMI linear redriver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TI_TDP2004_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TI_TDP2004_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TI_TDP2004_LOG_LEVEL_WRN"></a>

## 377.70 `CONFIG_TI_TDP2004_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TI_TDP2004_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → TDP2004 四通道 20 Gbps DisplayPort 2.1 和 12 Gbps HDMI 2.1 线性重驱动器（Linear Redriver） → TI TDP2004 DisplayPort 与 HDMI 线性重驱动器（TI TDP2004 DisplayPort and HDMI linear redriver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TI_TDP2004_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TI_TDP2004_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TLS_CREDENTIALS_LOG_LEVEL_CHOICE"></a>

## 377.71 `CONFIG_TLS_CREDENTIALS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：传输层安全凭据（tls_credentials）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_TLS_CREDENTIALS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_TLS_CREDENTIALS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_TLS_CREDENTIALS_LOG_LEVEL_OFF
CONFIG_TLS_CREDENTIALS_LOG_LEVEL_ERR
CONFIG_TLS_CREDENTIALS_LOG_LEVEL_WRN
CONFIG_TLS_CREDENTIALS_LOG_LEVEL_INF
CONFIG_TLS_CREDENTIALS_LOG_LEVEL_DBG
CONFIG_TLS_CREDENTIALS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 传输层安全（TLS）的凭据管理。

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_TLS_CREDENTIALS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TLS_CREDENTIALS)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_TLS_CREDENTIALS_LOG_LEVEL_DEFAULT`](P377_subsys_logging_配置项参考_26.md#CONFIG_TLS_CREDENTIALS_LOG_LEVEL_DEFAULT)、[`CONFIG_TLS_CREDENTIALS_LOG_LEVEL_OFF`](P377_subsys_logging_配置项参考_26.md#CONFIG_TLS_CREDENTIALS_LOG_LEVEL_OFF)、[`CONFIG_TLS_CREDENTIALS_LOG_LEVEL_ERR`](P377_subsys_logging_配置项参考_26.md#CONFIG_TLS_CREDENTIALS_LOG_LEVEL_ERR)、[`CONFIG_TLS_CREDENTIALS_LOG_LEVEL_WRN`](P377_subsys_logging_配置项参考_26.md#CONFIG_TLS_CREDENTIALS_LOG_LEVEL_WRN)、[`CONFIG_TLS_CREDENTIALS_LOG_LEVEL_INF`](P377_subsys_logging_配置项参考_26.md#CONFIG_TLS_CREDENTIALS_LOG_LEVEL_INF)、[`CONFIG_TLS_CREDENTIALS_LOG_LEVEL_DBG`](P377_subsys_logging_配置项参考_26.md#CONFIG_TLS_CREDENTIALS_LOG_LEVEL_DBG)。

<a id="CONFIG_TLS_CREDENTIALS_LOG_LEVEL_DBG"></a>

## 377.72 `CONFIG_TLS_CREDENTIALS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TLS_CREDENTIALS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 传输层安全（TLS）的凭据管理。 → 传输层安全凭据（tls_credentials）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TLS_CREDENTIALS_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TLS_CREDENTIALS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TLS_CREDENTIALS_LOG_LEVEL_DEFAULT"></a>

## 377.73 `CONFIG_TLS_CREDENTIALS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TLS_CREDENTIALS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 传输层安全（TLS）的凭据管理。 → 传输层安全凭据（tls_credentials）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TLS_CREDENTIALS_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TLS_CREDENTIALS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TLS_CREDENTIALS_LOG_LEVEL_ERR"></a>

## 377.74 `CONFIG_TLS_CREDENTIALS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TLS_CREDENTIALS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 传输层安全（TLS）的凭据管理。 → 传输层安全凭据（tls_credentials）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TLS_CREDENTIALS_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TLS_CREDENTIALS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TLS_CREDENTIALS_LOG_LEVEL_INF"></a>

## 377.75 `CONFIG_TLS_CREDENTIALS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TLS_CREDENTIALS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 传输层安全（TLS）的凭据管理。 → 传输层安全凭据（tls_credentials）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TLS_CREDENTIALS_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TLS_CREDENTIALS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TLS_CREDENTIALS_LOG_LEVEL_OFF"></a>

## 377.76 `CONFIG_TLS_CREDENTIALS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TLS_CREDENTIALS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 传输层安全（TLS）的凭据管理。 → 传输层安全凭据（tls_credentials）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TLS_CREDENTIALS_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TLS_CREDENTIALS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TLS_CREDENTIALS_LOG_LEVEL_WRN"></a>

## 377.77 `CONFIG_TLS_CREDENTIALS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TLS_CREDENTIALS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 传输层安全（TLS）的凭据管理。 → 传输层安全凭据（tls_credentials）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TLS_CREDENTIALS_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TLS_CREDENTIALS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TMC6460_LOG_LEVEL_CHOICE"></a>

## 377.78 `CONFIG_TMC6460_LOG_LEVEL_CHOICE`

**提示（Prompt）**：TMC6460 驱动（tmc6460）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_TMC6460
```

**默认值（Defaults）**

```text
CONFIG_TMC6460_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_TMC6460_LOG_LEVEL_OFF
CONFIG_TMC6460_LOG_LEVEL_ERR
CONFIG_TMC6460_LOG_LEVEL_WRN
CONFIG_TMC6460_LOG_LEVEL_INF
CONFIG_TMC6460_LOG_LEVEL_DBG
CONFIG_TMC6460_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Trinamic TMC6460 磁场定向控制（FOC）电机控制器

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_TMC6460`](P123_drivers_misc_配置项参考.md#CONFIG_TMC6460)、[`CONFIG_TMC6460_LOG_LEVEL_DEFAULT`](P377_subsys_logging_配置项参考_26.md#CONFIG_TMC6460_LOG_LEVEL_DEFAULT)、[`CONFIG_TMC6460_LOG_LEVEL_OFF`](P377_subsys_logging_配置项参考_26.md#CONFIG_TMC6460_LOG_LEVEL_OFF)、[`CONFIG_TMC6460_LOG_LEVEL_ERR`](P377_subsys_logging_配置项参考_26.md#CONFIG_TMC6460_LOG_LEVEL_ERR)、[`CONFIG_TMC6460_LOG_LEVEL_WRN`](P377_subsys_logging_配置项参考_26.md#CONFIG_TMC6460_LOG_LEVEL_WRN)、[`CONFIG_TMC6460_LOG_LEVEL_INF`](P377_subsys_logging_配置项参考_26.md#CONFIG_TMC6460_LOG_LEVEL_INF)、[`CONFIG_TMC6460_LOG_LEVEL_DBG`](P377_subsys_logging_配置项参考_26.md#CONFIG_TMC6460_LOG_LEVEL_DBG)。

<a id="CONFIG_TMC6460_LOG_LEVEL_DBG"></a>

## 377.79 `CONFIG_TMC6460_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TMC6460_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Trinamic TMC6460 磁场定向控制（FOC）电机控制器 → TMC6460 驱动（tmc6460）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TMC6460_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TMC6460_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TMC6460_LOG_LEVEL_DEFAULT"></a>

## 377.80 `CONFIG_TMC6460_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TMC6460_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Trinamic TMC6460 磁场定向控制（FOC）电机控制器 → TMC6460 驱动（tmc6460）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TMC6460_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TMC6460_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TMC6460_LOG_LEVEL_ERR"></a>

## 377.81 `CONFIG_TMC6460_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TMC6460_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Trinamic TMC6460 磁场定向控制（FOC）电机控制器 → TMC6460 驱动（tmc6460）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TMC6460_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TMC6460_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TMC6460_LOG_LEVEL_INF"></a>

## 377.82 `CONFIG_TMC6460_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TMC6460_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Trinamic TMC6460 磁场定向控制（FOC）电机控制器 → TMC6460 驱动（tmc6460）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TMC6460_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TMC6460_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TMC6460_LOG_LEVEL_OFF"></a>

## 377.83 `CONFIG_TMC6460_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TMC6460_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Trinamic TMC6460 磁场定向控制（FOC）电机控制器 → TMC6460 驱动（tmc6460）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TMC6460_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TMC6460_LOG_LEVEL_CHOICE)。

<a id="CONFIG_TMC6460_LOG_LEVEL_WRN"></a>

## 377.84 `CONFIG_TMC6460_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_TMC6460_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Trinamic TMC6460 磁场定向控制（FOC）电机控制器 → TMC6460 驱动（tmc6460）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_TMC6460_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_TMC6460_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UART_CONSOLE_LOG_LEVEL_CHOICE"></a>

## 377.85 `CONFIG_UART_CONSOLE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：UART 控制台（UART console）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_CONSOLE
```

**默认值（Defaults）**

```text
CONFIG_UART_CONSOLE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_UART_CONSOLE_LOG_LEVEL_OFF
CONFIG_UART_CONSOLE_LOG_LEVEL_ERR
CONFIG_UART_CONSOLE_LOG_LEVEL_WRN
CONFIG_UART_CONSOLE_LOG_LEVEL_INF
CONFIG_UART_CONSOLE_LOG_LEVEL_DBG
CONFIG_UART_CONSOLE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_CONSOLE`](P066_drivers_console_配置项参考.md#CONFIG_CONSOLE)、[`CONFIG_UART_CONSOLE_LOG_LEVEL_DEFAULT`](P377_subsys_logging_配置项参考_26.md#CONFIG_UART_CONSOLE_LOG_LEVEL_DEFAULT)、[`CONFIG_UART_CONSOLE_LOG_LEVEL_OFF`](P377_subsys_logging_配置项参考_26.md#CONFIG_UART_CONSOLE_LOG_LEVEL_OFF)、[`CONFIG_UART_CONSOLE_LOG_LEVEL_ERR`](P377_subsys_logging_配置项参考_26.md#CONFIG_UART_CONSOLE_LOG_LEVEL_ERR)、[`CONFIG_UART_CONSOLE_LOG_LEVEL_WRN`](P377_subsys_logging_配置项参考_26.md#CONFIG_UART_CONSOLE_LOG_LEVEL_WRN)、[`CONFIG_UART_CONSOLE_LOG_LEVEL_INF`](P377_subsys_logging_配置项参考_26.md#CONFIG_UART_CONSOLE_LOG_LEVEL_INF)、[`CONFIG_UART_CONSOLE_LOG_LEVEL_DBG`](P377_subsys_logging_配置项参考_26.md#CONFIG_UART_CONSOLE_LOG_LEVEL_DBG)。

<a id="CONFIG_UART_CONSOLE_LOG_LEVEL_DBG"></a>

## 377.86 `CONFIG_UART_CONSOLE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UART_CONSOLE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers） → UART 控制台（UART console）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UART_CONSOLE_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_UART_CONSOLE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UART_CONSOLE_LOG_LEVEL_DEFAULT"></a>

## 377.87 `CONFIG_UART_CONSOLE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UART_CONSOLE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers） → UART 控制台（UART console）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UART_CONSOLE_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_UART_CONSOLE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UART_CONSOLE_LOG_LEVEL_ERR"></a>

## 377.88 `CONFIG_UART_CONSOLE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UART_CONSOLE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers） → UART 控制台（UART console）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UART_CONSOLE_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_UART_CONSOLE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UART_CONSOLE_LOG_LEVEL_INF"></a>

## 377.89 `CONFIG_UART_CONSOLE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UART_CONSOLE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers） → UART 控制台（UART console）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UART_CONSOLE_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_UART_CONSOLE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UART_CONSOLE_LOG_LEVEL_OFF"></a>

## 377.90 `CONFIG_UART_CONSOLE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UART_CONSOLE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers） → UART 控制台（UART console）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UART_CONSOLE_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_UART_CONSOLE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UART_CONSOLE_LOG_LEVEL_WRN"></a>

## 377.91 `CONFIG_UART_CONSOLE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UART_CONSOLE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 控制台驱动（Console Drivers） → UART 控制台（UART console）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UART_CONSOLE_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_UART_CONSOLE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UART_LOG_LEVEL_CHOICE"></a>

## 377.92 `CONFIG_UART_LOG_LEVEL_CHOICE`

**提示（Prompt）**：通用异步收发器（uart）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_SERIAL
```

**默认值（Defaults）**

```text
CONFIG_UART_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_UART_LOG_LEVEL_OFF
CONFIG_UART_LOG_LEVEL_ERR
CONFIG_UART_LOG_LEVEL_WRN
CONFIG_UART_LOG_LEVEL_INF
CONFIG_UART_LOG_LEVEL_DBG
CONFIG_UART_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SERIAL`](P165_drivers_serial_配置项参考_1.md#CONFIG_SERIAL)、[`CONFIG_UART_LOG_LEVEL_DEFAULT`](P377_subsys_logging_配置项参考_26.md#CONFIG_UART_LOG_LEVEL_DEFAULT)、[`CONFIG_UART_LOG_LEVEL_OFF`](P377_subsys_logging_配置项参考_26.md#CONFIG_UART_LOG_LEVEL_OFF)、[`CONFIG_UART_LOG_LEVEL_ERR`](P377_subsys_logging_配置项参考_26.md#CONFIG_UART_LOG_LEVEL_ERR)、[`CONFIG_UART_LOG_LEVEL_WRN`](P377_subsys_logging_配置项参考_26.md#CONFIG_UART_LOG_LEVEL_WRN)、[`CONFIG_UART_LOG_LEVEL_INF`](P377_subsys_logging_配置项参考_26.md#CONFIG_UART_LOG_LEVEL_INF)、[`CONFIG_UART_LOG_LEVEL_DBG`](P377_subsys_logging_配置项参考_26.md#CONFIG_UART_LOG_LEVEL_DBG)。

<a id="CONFIG_UART_LOG_LEVEL_DBG"></a>

## 377.93 `CONFIG_UART_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UART_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → 通用异步收发器（uart）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UART_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_UART_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UART_LOG_LEVEL_DEFAULT"></a>

## 377.94 `CONFIG_UART_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UART_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → 通用异步收发器（uart）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UART_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_UART_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UART_LOG_LEVEL_ERR"></a>

## 377.95 `CONFIG_UART_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UART_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → 通用异步收发器（uart）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UART_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_UART_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UART_LOG_LEVEL_INF"></a>

## 377.96 `CONFIG_UART_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UART_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → 通用异步收发器（uart）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UART_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_UART_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UART_LOG_LEVEL_OFF"></a>

## 377.97 `CONFIG_UART_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UART_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → 通用异步收发器（uart）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UART_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_UART_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UART_LOG_LEVEL_WRN"></a>

## 377.98 `CONFIG_UART_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UART_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 串行驱动（Serial Drivers） → 通用异步收发器（uart）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UART_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_UART_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UDC_DRIVER_LOG_LEVEL_CHOICE"></a>

## 377.99 `CONFIG_UDC_DRIVER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB 驱动（usb drv）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_UDC_DRIVER
```

**默认值（Defaults）**

```text
CONFIG_UDC_DRIVER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_UDC_DRIVER_LOG_LEVEL_OFF
CONFIG_UDC_DRIVER_LOG_LEVEL_ERR
CONFIG_UDC_DRIVER_LOG_LEVEL_WRN
CONFIG_UDC_DRIVER_LOG_LEVEL_INF
CONFIG_UDC_DRIVER_LOG_LEVEL_DBG
CONFIG_UDC_DRIVER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_UDC_DRIVER`](P179_drivers_usb_配置项参考_1.md#CONFIG_UDC_DRIVER)、[`CONFIG_UDC_DRIVER_LOG_LEVEL_DEFAULT`](P378_subsys_logging_配置项参考_27.md#CONFIG_UDC_DRIVER_LOG_LEVEL_DEFAULT)、[`CONFIG_UDC_DRIVER_LOG_LEVEL_OFF`](P378_subsys_logging_配置项参考_27.md#CONFIG_UDC_DRIVER_LOG_LEVEL_OFF)、[`CONFIG_UDC_DRIVER_LOG_LEVEL_ERR`](P378_subsys_logging_配置项参考_27.md#CONFIG_UDC_DRIVER_LOG_LEVEL_ERR)、[`CONFIG_UDC_DRIVER_LOG_LEVEL_WRN`](P378_subsys_logging_配置项参考_27.md#CONFIG_UDC_DRIVER_LOG_LEVEL_WRN)、[`CONFIG_UDC_DRIVER_LOG_LEVEL_INF`](P378_subsys_logging_配置项参考_27.md#CONFIG_UDC_DRIVER_LOG_LEVEL_INF)、[`CONFIG_UDC_DRIVER_LOG_LEVEL_DBG`](P377_subsys_logging_配置项参考_26.md#CONFIG_UDC_DRIVER_LOG_LEVEL_DBG)。

<a id="CONFIG_UDC_DRIVER_LOG_LEVEL_DBG"></a>

## 377.100 `CONFIG_UDC_DRIVER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UDC_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → USB 驱动（usb drv）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UDC_DRIVER_LOG_LEVEL_CHOICE`](P377_subsys_logging_配置项参考_26.md#CONFIG_UDC_DRIVER_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P376_subsys_logging_配置项参考_25.md) · [返回大纲](大纲.md) · [下一章](P378_subsys_logging_配置项参考_27.md)
