---
id: learning.zephyr-docs.kconfig-reference.page-372
title: "`subsys/logging`配置项参考（21/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第372章\_`subsys/logging`配置项参考（21/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_MIPI_DSI_LOG_LEVEL_OFF"></a>

## 372.1 `CONFIG_MIPI_DSI_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MIPI_DSI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示串行接口（MIPI-DSI）主机控制器驱动【实验性】 → MIPI 显示串行接口（mipi_dsi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DSI_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MIPI_DSI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MIPI_DSI_LOG_LEVEL_WRN"></a>

## 372.2 `CONFIG_MIPI_DSI_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MIPI_DSI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → MIPI 显示串行接口（MIPI-DSI）主机控制器驱动【实验性】 → MIPI 显示串行接口（mipi_dsi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MIPI_DSI_LOG_LEVEL_CHOICE`](P371_subsys_logging_配置项参考_20.md#CONFIG_MIPI_DSI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MISC_MAX2221X_LOG_LEVEL_CHOICE"></a>

## 372.3 `CONFIG_MISC_MAX2221X_LOG_LEVEL_CHOICE`

**提示（Prompt）**：MAX2221x 杂项驱动（misc_max2221x）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MISC_MAX2221X
```

**默认值（Defaults）**

```text
CONFIG_MISC_MAX2221X_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MISC_MAX2221X_LOG_LEVEL_OFF
CONFIG_MISC_MAX2221X_LOG_LEVEL_ERR
CONFIG_MISC_MAX2221X_LOG_LEVEL_WRN
CONFIG_MISC_MAX2221X_LOG_LEVEL_INF
CONFIG_MISC_MAX2221X_LOG_LEVEL_DBG
CONFIG_MISC_MAX2221X_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Analog Devices MAX22216/MAX22217 杂项（Misc）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MISC_MAX2221X`](P123_drivers_misc_配置项参考.md#CONFIG_MISC_MAX2221X)、[`CONFIG_MISC_MAX2221X_LOG_LEVEL_DEFAULT`](P372_subsys_logging_配置项参考_21.md#CONFIG_MISC_MAX2221X_LOG_LEVEL_DEFAULT)、[`CONFIG_MISC_MAX2221X_LOG_LEVEL_OFF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MISC_MAX2221X_LOG_LEVEL_OFF)、[`CONFIG_MISC_MAX2221X_LOG_LEVEL_ERR`](P372_subsys_logging_配置项参考_21.md#CONFIG_MISC_MAX2221X_LOG_LEVEL_ERR)、[`CONFIG_MISC_MAX2221X_LOG_LEVEL_WRN`](P372_subsys_logging_配置项参考_21.md#CONFIG_MISC_MAX2221X_LOG_LEVEL_WRN)、[`CONFIG_MISC_MAX2221X_LOG_LEVEL_INF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MISC_MAX2221X_LOG_LEVEL_INF)、[`CONFIG_MISC_MAX2221X_LOG_LEVEL_DBG`](P372_subsys_logging_配置项参考_21.md#CONFIG_MISC_MAX2221X_LOG_LEVEL_DBG)。

<a id="CONFIG_MISC_MAX2221X_LOG_LEVEL_DBG"></a>

## 372.4 `CONFIG_MISC_MAX2221X_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MISC_MAX2221X_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Analog Devices MAX22216/MAX22217 杂项（Misc）驱动 → MAX2221x 杂项驱动（misc_max2221x）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MISC_MAX2221X_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MISC_MAX2221X_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MISC_MAX2221X_LOG_LEVEL_DEFAULT"></a>

## 372.5 `CONFIG_MISC_MAX2221X_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MISC_MAX2221X_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Analog Devices MAX22216/MAX22217 杂项（Misc）驱动 → MAX2221x 杂项驱动（misc_max2221x）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MISC_MAX2221X_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MISC_MAX2221X_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MISC_MAX2221X_LOG_LEVEL_ERR"></a>

## 372.6 `CONFIG_MISC_MAX2221X_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MISC_MAX2221X_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Analog Devices MAX22216/MAX22217 杂项（Misc）驱动 → MAX2221x 杂项驱动（misc_max2221x）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MISC_MAX2221X_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MISC_MAX2221X_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MISC_MAX2221X_LOG_LEVEL_INF"></a>

## 372.7 `CONFIG_MISC_MAX2221X_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MISC_MAX2221X_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Analog Devices MAX22216/MAX22217 杂项（Misc）驱动 → MAX2221x 杂项驱动（misc_max2221x）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MISC_MAX2221X_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MISC_MAX2221X_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MISC_MAX2221X_LOG_LEVEL_OFF"></a>

## 372.8 `CONFIG_MISC_MAX2221X_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MISC_MAX2221X_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Analog Devices MAX22216/MAX22217 杂项（Misc）驱动 → MAX2221x 杂项驱动（misc_max2221x）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MISC_MAX2221X_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MISC_MAX2221X_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MISC_MAX2221X_LOG_LEVEL_WRN"></a>

## 372.9 `CONFIG_MISC_MAX2221X_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MISC_MAX2221X_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Analog Devices MAX22216/MAX22217 杂项（Misc）驱动 → MAX2221x 杂项驱动（misc_max2221x）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MISC_MAX2221X_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MISC_MAX2221X_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MMC_LOG_LEVEL_CHOICE"></a>

## 372.10 `CONFIG_MMC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：多媒体卡（mmc）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_DISK_DRIVER_MMC && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_MMC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MMC_LOG_LEVEL_OFF
CONFIG_MMC_LOG_LEVEL_ERR
CONFIG_MMC_LOG_LEVEL_WRN
CONFIG_MMC_LOG_LEVEL_INF
CONFIG_MMC_LOG_LEVEL_DBG
CONFIG_MMC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → MMC 卡驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_DISK_DRIVER_MMC`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_MMC)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)、[`CONFIG_MMC_LOG_LEVEL_DEFAULT`](P372_subsys_logging_配置项参考_21.md#CONFIG_MMC_LOG_LEVEL_DEFAULT)、[`CONFIG_MMC_LOG_LEVEL_OFF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MMC_LOG_LEVEL_OFF)、[`CONFIG_MMC_LOG_LEVEL_ERR`](P372_subsys_logging_配置项参考_21.md#CONFIG_MMC_LOG_LEVEL_ERR)、[`CONFIG_MMC_LOG_LEVEL_WRN`](P372_subsys_logging_配置项参考_21.md#CONFIG_MMC_LOG_LEVEL_WRN)、[`CONFIG_MMC_LOG_LEVEL_INF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MMC_LOG_LEVEL_INF)、[`CONFIG_MMC_LOG_LEVEL_DBG`](P372_subsys_logging_配置项参考_21.md#CONFIG_MMC_LOG_LEVEL_DBG)。

<a id="CONFIG_MMC_LOG_LEVEL_DBG"></a>

## 372.11 `CONFIG_MMC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MMC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → MMC 卡驱动 → 多媒体卡（mmc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MMC_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MMC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MMC_LOG_LEVEL_DEFAULT"></a>

## 372.12 `CONFIG_MMC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MMC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → MMC 卡驱动 → 多媒体卡（mmc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MMC_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MMC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MMC_LOG_LEVEL_ERR"></a>

## 372.13 `CONFIG_MMC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MMC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → MMC 卡驱动 → 多媒体卡（mmc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MMC_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MMC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MMC_LOG_LEVEL_INF"></a>

## 372.14 `CONFIG_MMC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MMC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → MMC 卡驱动 → 多媒体卡（mmc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MMC_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MMC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MMC_LOG_LEVEL_OFF"></a>

## 372.15 `CONFIG_MMC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MMC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → MMC 卡驱动 → 多媒体卡（mmc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MMC_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MMC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MMC_LOG_LEVEL_WRN"></a>

## 372.16 `CONFIG_MMC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MMC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → MMC 卡驱动 → 多媒体卡（mmc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MMC_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MMC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODBUS_LOG_LEVEL_CHOICE"></a>

## 372.17 `CONFIG_MODBUS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：Modbus 支持（Modbus Support）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MODBUS
```

**默认值（Defaults）**

```text
CONFIG_MODBUS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MODBUS_LOG_LEVEL_OFF
CONFIG_MODBUS_LOG_LEVEL_ERR
CONFIG_MODBUS_LOG_LEVEL_WRN
CONFIG_MODBUS_LOG_LEVEL_INF
CONFIG_MODBUS_LOG_LEVEL_DBG
CONFIG_MODBUS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → Modbus 支持（support）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MODBUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODBUS)、[`CONFIG_MODBUS_LOG_LEVEL_DEFAULT`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODBUS_LOG_LEVEL_DEFAULT)、[`CONFIG_MODBUS_LOG_LEVEL_OFF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODBUS_LOG_LEVEL_OFF)、[`CONFIG_MODBUS_LOG_LEVEL_ERR`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODBUS_LOG_LEVEL_ERR)、[`CONFIG_MODBUS_LOG_LEVEL_WRN`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODBUS_LOG_LEVEL_WRN)、[`CONFIG_MODBUS_LOG_LEVEL_INF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODBUS_LOG_LEVEL_INF)、[`CONFIG_MODBUS_LOG_LEVEL_DBG`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODBUS_LOG_LEVEL_DBG)。

<a id="CONFIG_MODBUS_LOG_LEVEL_DBG"></a>

## 372.18 `CONFIG_MODBUS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODBUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → Modbus 支持（support） → Modbus 支持（Modbus Support）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODBUS_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODBUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODBUS_LOG_LEVEL_DEFAULT"></a>

## 372.19 `CONFIG_MODBUS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODBUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → Modbus 支持（support） → Modbus 支持（Modbus Support）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODBUS_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODBUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODBUS_LOG_LEVEL_ERR"></a>

## 372.20 `CONFIG_MODBUS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODBUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → Modbus 支持（support） → Modbus 支持（Modbus Support）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODBUS_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODBUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODBUS_LOG_LEVEL_INF"></a>

## 372.21 `CONFIG_MODBUS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODBUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → Modbus 支持（support） → Modbus 支持（Modbus Support）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODBUS_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODBUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODBUS_LOG_LEVEL_OFF"></a>

## 372.22 `CONFIG_MODBUS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODBUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → Modbus 支持（support） → Modbus 支持（Modbus Support）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODBUS_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODBUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODBUS_LOG_LEVEL_WRN"></a>

## 372.23 `CONFIG_MODBUS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODBUS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → Modbus 支持（support） → Modbus 支持（Modbus Support）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODBUS_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODBUS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODEM_CMUX_LOG_LEVEL_CHOICE"></a>

## 372.24 `CONFIG_MODEM_CMUX_LOG_LEVEL_CHOICE`

**提示（Prompt）**：调制解调器连接复用（modem_cmux）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MODEM_CMUX && CONFIG_MODEM_MODULES
```

**默认值（Defaults）**

```text
CONFIG_MODEM_CMUX_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MODEM_CMUX_LOG_LEVEL_OFF
CONFIG_MODEM_CMUX_LOG_LEVEL_ERR
CONFIG_MODEM_CMUX_LOG_LEVEL_WRN
CONFIG_MODEM_CMUX_LOG_LEVEL_INF
CONFIG_MODEM_CMUX_LOG_LEVEL_DBG
CONFIG_MODEM_CMUX_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器连接复用模块（Modem CMUX module）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MODEM_CMUX`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_CMUX)、[`CONFIG_MODEM_MODULES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_MODULES)、[`CONFIG_MODEM_CMUX_LOG_LEVEL_DEFAULT`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_CMUX_LOG_LEVEL_DEFAULT)、[`CONFIG_MODEM_CMUX_LOG_LEVEL_OFF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_CMUX_LOG_LEVEL_OFF)、[`CONFIG_MODEM_CMUX_LOG_LEVEL_ERR`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_CMUX_LOG_LEVEL_ERR)、[`CONFIG_MODEM_CMUX_LOG_LEVEL_WRN`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_CMUX_LOG_LEVEL_WRN)、[`CONFIG_MODEM_CMUX_LOG_LEVEL_INF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_CMUX_LOG_LEVEL_INF)、[`CONFIG_MODEM_CMUX_LOG_LEVEL_DBG`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_CMUX_LOG_LEVEL_DBG)。

<a id="CONFIG_MODEM_CMUX_LOG_LEVEL_DBG"></a>

## 372.25 `CONFIG_MODEM_CMUX_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_CMUX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器连接复用模块（Modem CMUX module） → 调制解调器连接复用（modem_cmux）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CMUX_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_CMUX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODEM_CMUX_LOG_LEVEL_DEFAULT"></a>

## 372.26 `CONFIG_MODEM_CMUX_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_CMUX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器连接复用模块（Modem CMUX module） → 调制解调器连接复用（modem_cmux）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CMUX_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_CMUX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODEM_CMUX_LOG_LEVEL_ERR"></a>

## 372.27 `CONFIG_MODEM_CMUX_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_CMUX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器连接复用模块（Modem CMUX module） → 调制解调器连接复用（modem_cmux）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CMUX_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_CMUX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODEM_CMUX_LOG_LEVEL_INF"></a>

## 372.28 `CONFIG_MODEM_CMUX_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_CMUX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器连接复用模块（Modem CMUX module） → 调制解调器连接复用（modem_cmux）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CMUX_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_CMUX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODEM_CMUX_LOG_LEVEL_OFF"></a>

## 372.29 `CONFIG_MODEM_CMUX_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_CMUX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器连接复用模块（Modem CMUX module） → 调制解调器连接复用（modem_cmux）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CMUX_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_CMUX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODEM_CMUX_LOG_LEVEL_WRN"></a>

## 372.30 `CONFIG_MODEM_CMUX_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_CMUX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器连接复用模块（Modem CMUX module） → 调制解调器连接复用（modem_cmux）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_CMUX_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_CMUX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODEM_LOG_LEVEL_CHOICE"></a>

## 372.31 `CONFIG_MODEM_LOG_LEVEL_CHOICE`

**提示（Prompt）**：调制解调器（modem）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MODEM
```

**默认值（Defaults）**

```text
CONFIG_MODEM_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MODEM_LOG_LEVEL_OFF
CONFIG_MODEM_LOG_LEVEL_ERR
CONFIG_MODEM_LOG_LEVEL_WRN
CONFIG_MODEM_LOG_LEVEL_INF
CONFIG_MODEM_LOG_LEVEL_DBG
CONFIG_MODEM_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_LOG_LEVEL_DEFAULT`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_LOG_LEVEL_DEFAULT)、[`CONFIG_MODEM_LOG_LEVEL_OFF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_LOG_LEVEL_OFF)、[`CONFIG_MODEM_LOG_LEVEL_ERR`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_LOG_LEVEL_ERR)、[`CONFIG_MODEM_LOG_LEVEL_WRN`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_LOG_LEVEL_WRN)、[`CONFIG_MODEM_LOG_LEVEL_INF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_LOG_LEVEL_INF)、[`CONFIG_MODEM_LOG_LEVEL_DBG`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_LOG_LEVEL_DBG)。

<a id="CONFIG_MODEM_LOG_LEVEL_DBG"></a>

## 372.32 `CONFIG_MODEM_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 调制解调器（modem）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODEM_LOG_LEVEL_DEFAULT"></a>

## 372.33 `CONFIG_MODEM_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 调制解调器（modem）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODEM_LOG_LEVEL_ERR"></a>

## 372.34 `CONFIG_MODEM_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 调制解调器（modem）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODEM_LOG_LEVEL_INF"></a>

## 372.35 `CONFIG_MODEM_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 调制解调器（modem）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODEM_LOG_LEVEL_OFF"></a>

## 372.36 `CONFIG_MODEM_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 调制解调器（modem）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODEM_LOG_LEVEL_WRN"></a>

## 372.37 `CONFIG_MODEM_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → 调制解调器（modem）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODEM_MODULES_LOG_LEVEL_CHOICE"></a>

## 372.38 `CONFIG_MODEM_MODULES_LOG_LEVEL_CHOICE`

**提示（Prompt）**：调制解调器模块（modem_modules）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MODEM_MODULES
```

**默认值（Defaults）**

```text
CONFIG_MODEM_MODULES_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MODEM_MODULES_LOG_LEVEL_OFF
CONFIG_MODEM_MODULES_LOG_LEVEL_ERR
CONFIG_MODEM_MODULES_LOG_LEVEL_WRN
CONFIG_MODEM_MODULES_LOG_LEVEL_INF
CONFIG_MODEM_MODULES_LOG_LEVEL_DBG
CONFIG_MODEM_MODULES_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MODEM_MODULES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MODEM_MODULES)、[`CONFIG_MODEM_MODULES_LOG_LEVEL_DEFAULT`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_MODULES_LOG_LEVEL_DEFAULT)、[`CONFIG_MODEM_MODULES_LOG_LEVEL_OFF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_MODULES_LOG_LEVEL_OFF)、[`CONFIG_MODEM_MODULES_LOG_LEVEL_ERR`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_MODULES_LOG_LEVEL_ERR)、[`CONFIG_MODEM_MODULES_LOG_LEVEL_WRN`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_MODULES_LOG_LEVEL_WRN)、[`CONFIG_MODEM_MODULES_LOG_LEVEL_INF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_MODULES_LOG_LEVEL_INF)、[`CONFIG_MODEM_MODULES_LOG_LEVEL_DBG`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_MODULES_LOG_LEVEL_DBG)。

<a id="CONFIG_MODEM_MODULES_LOG_LEVEL_DBG"></a>

## 372.39 `CONFIG_MODEM_MODULES_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_MODULES_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器模块（modem_modules）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_MODULES_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_MODULES_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODEM_MODULES_LOG_LEVEL_DEFAULT"></a>

## 372.40 `CONFIG_MODEM_MODULES_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_MODULES_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器模块（modem_modules）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_MODULES_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_MODULES_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODEM_MODULES_LOG_LEVEL_ERR"></a>

## 372.41 `CONFIG_MODEM_MODULES_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_MODULES_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器模块（modem_modules）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_MODULES_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_MODULES_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODEM_MODULES_LOG_LEVEL_INF"></a>

## 372.42 `CONFIG_MODEM_MODULES_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_MODULES_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器模块（modem_modules）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_MODULES_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_MODULES_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODEM_MODULES_LOG_LEVEL_OFF"></a>

## 372.43 `CONFIG_MODEM_MODULES_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_MODULES_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器模块（modem_modules）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_MODULES_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_MODULES_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODEM_MODULES_LOG_LEVEL_WRN"></a>

## 372.44 `CONFIG_MODEM_MODULES_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_MODULES_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 调制解调器模块（Modem modules） → 调制解调器模块（modem_modules）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_MODULES_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_MODULES_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_CHOICE"></a>

## 372.45 `CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_CHOICE`

**提示（Prompt）**：Quectel BC66x 调制解调器（modem-quectel-bc66x）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MODEM_QUECTEL_BC66X && CONFIG_MODEM
```

**默认值（Defaults）**

```text
CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_OFF
CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_ERR
CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_WRN
CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_INF
CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_DBG
CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel BC66 / BC660K 窄带物联网（NB-IoT）调制解调器驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MODEM_QUECTEL_BC66X`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_QUECTEL_BC66X)、[`CONFIG_MODEM`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM)、[`CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_DEFAULT`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_DEFAULT)、[`CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_OFF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_OFF)、[`CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_ERR`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_ERR)、[`CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_WRN`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_WRN)、[`CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_INF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_INF)、[`CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_DBG`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_DBG)。

<a id="CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_DBG"></a>

## 372.46 `CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel BC66 / BC660K 窄带物联网（NB-IoT）调制解调器驱动 → Quectel BC66x 调制解调器（modem-quectel-bc66x）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_DEFAULT"></a>

## 372.47 `CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel BC66 / BC660K 窄带物联网（NB-IoT）调制解调器驱动 → Quectel BC66x 调制解调器（modem-quectel-bc66x）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_ERR"></a>

## 372.48 `CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel BC66 / BC660K 窄带物联网（NB-IoT）调制解调器驱动 → Quectel BC66x 调制解调器（modem-quectel-bc66x）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_INF"></a>

## 372.49 `CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel BC66 / BC660K 窄带物联网（NB-IoT）调制解调器驱动 → Quectel BC66x 调制解调器（modem-quectel-bc66x）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_OFF"></a>

## 372.50 `CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel BC66 / BC660K 窄带物联网（NB-IoT）调制解调器驱动 → Quectel BC66x 调制解调器（modem-quectel-bc66x）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_WRN"></a>

## 372.51 `CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调制解调器驱动（Modem Drivers） → Quectel BC66 / BC660K 窄带物联网（NB-IoT）调制解调器驱动 → Quectel BC66x 调制解调器（modem-quectel-bc66x）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MODEM_QUECTEL_BC66X_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MPIPE_LOG_LEVEL_CHOICE"></a>

## 372.52 `CONFIG_MPIPE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：多媒体流水线（mpipe）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MPIPE
```

**默认值（Defaults）**

```text
CONFIG_MPIPE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MPIPE_LOG_LEVEL_OFF
CONFIG_MPIPE_LOG_LEVEL_ERR
CONFIG_MPIPE_LOG_LEVEL_WRN
CONFIG_MPIPE_LOG_LEVEL_INF
CONFIG_MPIPE_LOG_LEVEL_DBG
CONFIG_MPIPE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MPIPE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MPIPE)、[`CONFIG_MPIPE_LOG_LEVEL_DEFAULT`](P372_subsys_logging_配置项参考_21.md#CONFIG_MPIPE_LOG_LEVEL_DEFAULT)、[`CONFIG_MPIPE_LOG_LEVEL_OFF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MPIPE_LOG_LEVEL_OFF)、[`CONFIG_MPIPE_LOG_LEVEL_ERR`](P372_subsys_logging_配置项参考_21.md#CONFIG_MPIPE_LOG_LEVEL_ERR)、[`CONFIG_MPIPE_LOG_LEVEL_WRN`](P372_subsys_logging_配置项参考_21.md#CONFIG_MPIPE_LOG_LEVEL_WRN)、[`CONFIG_MPIPE_LOG_LEVEL_INF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MPIPE_LOG_LEVEL_INF)、[`CONFIG_MPIPE_LOG_LEVEL_DBG`](P372_subsys_logging_配置项参考_21.md#CONFIG_MPIPE_LOG_LEVEL_DBG)。

<a id="CONFIG_MPIPE_LOG_LEVEL_DBG"></a>

## 372.53 `CONFIG_MPIPE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MPIPE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】 → 多媒体流水线（mpipe）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MPIPE_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MPIPE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MPIPE_LOG_LEVEL_DEFAULT"></a>

## 372.54 `CONFIG_MPIPE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MPIPE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】 → 多媒体流水线（mpipe）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MPIPE_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MPIPE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MPIPE_LOG_LEVEL_ERR"></a>

## 372.55 `CONFIG_MPIPE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MPIPE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】 → 多媒体流水线（mpipe）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MPIPE_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MPIPE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MPIPE_LOG_LEVEL_INF"></a>

## 372.56 `CONFIG_MPIPE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MPIPE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】 → 多媒体流水线（mpipe）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MPIPE_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MPIPE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MPIPE_LOG_LEVEL_OFF"></a>

## 372.57 `CONFIG_MPIPE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MPIPE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】 → 多媒体流水线（mpipe）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MPIPE_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MPIPE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MPIPE_LOG_LEVEL_WRN"></a>

## 372.58 `CONFIG_MPIPE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MPIPE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 多媒体流水线框架（Multimedia Pipeline framework）【实验性 EXPERIMENTAL】 → 多媒体流水线（mpipe）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MPIPE_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MPIPE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MPU_LOG_LEVEL_CHOICE"></a>

## 372.59 `CONFIG_MPU_LOG_LEVEL_CHOICE`

**提示（Prompt）**：内存保护单元（mpu）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MPU
```

**默认值（Defaults）**

```text
CONFIG_MPU_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MPU_LOG_LEVEL_OFF
CONFIG_MPU_LOG_LEVEL_ERR
CONFIG_MPU_LOG_LEVEL_WRN
CONFIG_MPU_LOG_LEVEL_INF
CONFIG_MPU_LOG_LEVEL_DBG
CONFIG_MPU_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 内存保护单元功能（MPU Features）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MPU`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_MPU)、[`CONFIG_MPU_LOG_LEVEL_DEFAULT`](P372_subsys_logging_配置项参考_21.md#CONFIG_MPU_LOG_LEVEL_DEFAULT)、[`CONFIG_MPU_LOG_LEVEL_OFF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MPU_LOG_LEVEL_OFF)、[`CONFIG_MPU_LOG_LEVEL_ERR`](P372_subsys_logging_配置项参考_21.md#CONFIG_MPU_LOG_LEVEL_ERR)、[`CONFIG_MPU_LOG_LEVEL_WRN`](P372_subsys_logging_配置项参考_21.md#CONFIG_MPU_LOG_LEVEL_WRN)、[`CONFIG_MPU_LOG_LEVEL_INF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MPU_LOG_LEVEL_INF)、[`CONFIG_MPU_LOG_LEVEL_DBG`](P372_subsys_logging_配置项参考_21.md#CONFIG_MPU_LOG_LEVEL_DBG)。

<a id="CONFIG_MPU_LOG_LEVEL_DBG"></a>

## 372.60 `CONFIG_MPU_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MPU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 内存保护单元功能（MPU Features） → 内存保护单元（mpu）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MPU_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MPU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MPU_LOG_LEVEL_DEFAULT"></a>

## 372.61 `CONFIG_MPU_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MPU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 内存保护单元功能（MPU Features） → 内存保护单元（mpu）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MPU_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MPU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MPU_LOG_LEVEL_ERR"></a>

## 372.62 `CONFIG_MPU_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MPU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 内存保护单元功能（MPU Features） → 内存保护单元（mpu）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MPU_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MPU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MPU_LOG_LEVEL_INF"></a>

## 372.63 `CONFIG_MPU_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MPU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 内存保护单元功能（MPU Features） → 内存保护单元（mpu）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MPU_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MPU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MPU_LOG_LEVEL_OFF"></a>

## 372.64 `CONFIG_MPU_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MPU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 内存保护单元功能（MPU Features） → 内存保护单元（mpu）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MPU_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MPU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MPU_LOG_LEVEL_WRN"></a>

## 372.65 `CONFIG_MPU_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MPU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 内存保护单元功能（MPU Features） → 内存保护单元（mpu）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MPU_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MPU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MRAM_LATENCY_LOG_LEVEL_CHOICE"></a>

## 372.66 `CONFIG_MRAM_LATENCY_LOG_LEVEL_CHOICE`

**提示（Prompt）**：磁阻式 RAM 延迟（mram_latency）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MRAM_LATENCY && CONFIG_SOC_FAMILY_NORDIC_NRF
```

**默认值（Defaults）**

```text
CONFIG_MRAM_LATENCY_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MRAM_LATENCY_LOG_LEVEL_OFF
CONFIG_MRAM_LATENCY_LOG_LEVEL_ERR
CONFIG_MRAM_LATENCY_LOG_LEVEL_WRN
CONFIG_MRAM_LATENCY_LOG_LEVEL_INF
CONFIG_MRAM_LATENCY_LOG_LEVEL_DBG
CONFIG_MRAM_LATENCY_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 磁阻 RAM 延迟管理器（MRAM latency manager）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MRAM_LATENCY`](P289_soc_nordic_配置项参考_1.md#CONFIG_MRAM_LATENCY)、[`CONFIG_SOC_FAMILY_NORDIC_NRF`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_NORDIC_NRF)、[`CONFIG_MRAM_LATENCY_LOG_LEVEL_DEFAULT`](P372_subsys_logging_配置项参考_21.md#CONFIG_MRAM_LATENCY_LOG_LEVEL_DEFAULT)、[`CONFIG_MRAM_LATENCY_LOG_LEVEL_OFF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MRAM_LATENCY_LOG_LEVEL_OFF)、[`CONFIG_MRAM_LATENCY_LOG_LEVEL_ERR`](P372_subsys_logging_配置项参考_21.md#CONFIG_MRAM_LATENCY_LOG_LEVEL_ERR)、[`CONFIG_MRAM_LATENCY_LOG_LEVEL_WRN`](P372_subsys_logging_配置项参考_21.md#CONFIG_MRAM_LATENCY_LOG_LEVEL_WRN)、[`CONFIG_MRAM_LATENCY_LOG_LEVEL_INF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MRAM_LATENCY_LOG_LEVEL_INF)、[`CONFIG_MRAM_LATENCY_LOG_LEVEL_DBG`](P372_subsys_logging_配置项参考_21.md#CONFIG_MRAM_LATENCY_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_NORDIC_NRF`。

<a id="CONFIG_MRAM_LATENCY_LOG_LEVEL_DBG"></a>

## 372.67 `CONFIG_MRAM_LATENCY_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MRAM_LATENCY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 磁阻 RAM 延迟管理器（MRAM latency manager） → 磁阻式 RAM 延迟（mram_latency）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MRAM_LATENCY_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MRAM_LATENCY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MRAM_LATENCY_LOG_LEVEL_DEFAULT"></a>

## 372.68 `CONFIG_MRAM_LATENCY_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MRAM_LATENCY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 磁阻 RAM 延迟管理器（MRAM latency manager） → 磁阻式 RAM 延迟（mram_latency）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MRAM_LATENCY_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MRAM_LATENCY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MRAM_LATENCY_LOG_LEVEL_ERR"></a>

## 372.69 `CONFIG_MRAM_LATENCY_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MRAM_LATENCY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 磁阻 RAM 延迟管理器（MRAM latency manager） → 磁阻式 RAM 延迟（mram_latency）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MRAM_LATENCY_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MRAM_LATENCY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MRAM_LATENCY_LOG_LEVEL_INF"></a>

## 372.70 `CONFIG_MRAM_LATENCY_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MRAM_LATENCY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 磁阻 RAM 延迟管理器（MRAM latency manager） → 磁阻式 RAM 延迟（mram_latency）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MRAM_LATENCY_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MRAM_LATENCY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MRAM_LATENCY_LOG_LEVEL_OFF"></a>

## 372.71 `CONFIG_MRAM_LATENCY_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MRAM_LATENCY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 磁阻 RAM 延迟管理器（MRAM latency manager） → 磁阻式 RAM 延迟（mram_latency）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MRAM_LATENCY_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MRAM_LATENCY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MRAM_LATENCY_LOG_LEVEL_WRN"></a>

## 372.72 `CONFIG_MRAM_LATENCY_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MRAM_LATENCY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 硬件配置（Hardware Configuration） → 磁阻 RAM 延迟管理器（MRAM latency manager） → 磁阻式 RAM 延迟（mram_latency）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MRAM_LATENCY_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MRAM_LATENCY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MSPI_LOG_LEVEL_CHOICE"></a>

## 372.73 `CONFIG_MSPI_LOG_LEVEL_CHOICE`

**提示（Prompt）**：多线串行外设接口（mspi）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MSPI
```

**默认值（Defaults）**

```text
CONFIG_MSPI_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MSPI_LOG_LEVEL_OFF
CONFIG_MSPI_LOG_LEVEL_ERR
CONFIG_MSPI_LOG_LEVEL_WRN
CONFIG_MSPI_LOG_LEVEL_INF
CONFIG_MSPI_LOG_LEVEL_DBG
CONFIG_MSPI_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MSPI`](P129_drivers_mspi_配置项参考.md#CONFIG_MSPI)、[`CONFIG_MSPI_LOG_LEVEL_DEFAULT`](P372_subsys_logging_配置项参考_21.md#CONFIG_MSPI_LOG_LEVEL_DEFAULT)、[`CONFIG_MSPI_LOG_LEVEL_OFF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MSPI_LOG_LEVEL_OFF)、[`CONFIG_MSPI_LOG_LEVEL_ERR`](P372_subsys_logging_配置项参考_21.md#CONFIG_MSPI_LOG_LEVEL_ERR)、[`CONFIG_MSPI_LOG_LEVEL_WRN`](P372_subsys_logging_配置项参考_21.md#CONFIG_MSPI_LOG_LEVEL_WRN)、[`CONFIG_MSPI_LOG_LEVEL_INF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MSPI_LOG_LEVEL_INF)、[`CONFIG_MSPI_LOG_LEVEL_DBG`](P372_subsys_logging_配置项参考_21.md#CONFIG_MSPI_LOG_LEVEL_DBG)。

<a id="CONFIG_MSPI_LOG_LEVEL_DBG"></a>

## 372.74 `CONFIG_MSPI_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MSPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动 → 多线串行外设接口（mspi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MSPI_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MSPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MSPI_LOG_LEVEL_DEFAULT"></a>

## 372.75 `CONFIG_MSPI_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MSPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动 → 多线串行外设接口（mspi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MSPI_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MSPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MSPI_LOG_LEVEL_ERR"></a>

## 372.76 `CONFIG_MSPI_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MSPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动 → 多线串行外设接口（mspi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MSPI_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MSPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MSPI_LOG_LEVEL_INF"></a>

## 372.77 `CONFIG_MSPI_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MSPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动 → 多线串行外设接口（mspi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MSPI_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MSPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MSPI_LOG_LEVEL_OFF"></a>

## 372.78 `CONFIG_MSPI_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MSPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动 → 多线串行外设接口（mspi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MSPI_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MSPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MSPI_LOG_LEVEL_WRN"></a>

## 372.79 `CONFIG_MSPI_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MSPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多位串行外设接口（Multi-bit Serial Peripheral Interface，MSPI）总线驱动 → 多线串行外设接口（mspi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MSPI_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MSPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MTCH9010_LOG_LEVEL_CHOICE"></a>

## 372.80 `CONFIG_MTCH9010_LOG_LEVEL_CHOICE`

**提示（Prompt）**：MTCH9010 驱动（MTCH9010）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MTCH9010 && CONFIG_SENSOR
```

**默认值（Defaults）**

```text
CONFIG_MTCH9010_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MTCH9010_LOG_LEVEL_OFF
CONFIG_MTCH9010_LOG_LEVEL_ERR
CONFIG_MTCH9010_LOG_LEVEL_WRN
CONFIG_MTCH9010_LOG_LEVEL_INF
CONFIG_MTCH9010_LOG_LEVEL_DBG
CONFIG_MTCH9010_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MTCH9010

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MTCH9010`](P159_drivers_sensor_配置项参考_11.md#CONFIG_MTCH9010)、[`CONFIG_SENSOR`](P160_drivers_sensor_配置项参考_12.md#CONFIG_SENSOR)、[`CONFIG_MTCH9010_LOG_LEVEL_DEFAULT`](P372_subsys_logging_配置项参考_21.md#CONFIG_MTCH9010_LOG_LEVEL_DEFAULT)、[`CONFIG_MTCH9010_LOG_LEVEL_OFF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MTCH9010_LOG_LEVEL_OFF)、[`CONFIG_MTCH9010_LOG_LEVEL_ERR`](P372_subsys_logging_配置项参考_21.md#CONFIG_MTCH9010_LOG_LEVEL_ERR)、[`CONFIG_MTCH9010_LOG_LEVEL_WRN`](P372_subsys_logging_配置项参考_21.md#CONFIG_MTCH9010_LOG_LEVEL_WRN)、[`CONFIG_MTCH9010_LOG_LEVEL_INF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MTCH9010_LOG_LEVEL_INF)、[`CONFIG_MTCH9010_LOG_LEVEL_DBG`](P372_subsys_logging_配置项参考_21.md#CONFIG_MTCH9010_LOG_LEVEL_DBG)。

<a id="CONFIG_MTCH9010_LOG_LEVEL_DBG"></a>

## 372.81 `CONFIG_MTCH9010_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MTCH9010_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MTCH9010 → MTCH9010 驱动（MTCH9010）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MTCH9010_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MTCH9010_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MTCH9010_LOG_LEVEL_DEFAULT"></a>

## 372.82 `CONFIG_MTCH9010_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MTCH9010_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MTCH9010 → MTCH9010 驱动（MTCH9010）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MTCH9010_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MTCH9010_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MTCH9010_LOG_LEVEL_ERR"></a>

## 372.83 `CONFIG_MTCH9010_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MTCH9010_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MTCH9010 → MTCH9010 驱动（MTCH9010）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MTCH9010_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MTCH9010_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MTCH9010_LOG_LEVEL_INF"></a>

## 372.84 `CONFIG_MTCH9010_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MTCH9010_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MTCH9010 → MTCH9010 驱动（MTCH9010）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MTCH9010_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MTCH9010_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MTCH9010_LOG_LEVEL_OFF"></a>

## 372.85 `CONFIG_MTCH9010_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MTCH9010_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MTCH9010 → MTCH9010 驱动（MTCH9010）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MTCH9010_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MTCH9010_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MTCH9010_LOG_LEVEL_WRN"></a>

## 372.86 `CONFIG_MTCH9010_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MTCH9010_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 传感器驱动（Sensor Drivers） → MTCH9010 → MTCH9010 驱动（MTCH9010）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MTCH9010_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MTCH9010_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MTRACE_LOG_CACHE_BUF_SIZE"></a>

## 372.87 `CONFIG_MTRACE_LOG_CACHE_BUF_SIZE`

**提示（Prompt）**：为 mtrace 日志缓存缓冲区分配的字节数

**说明（Help）**

专用于 mtrace 日志缓存缓冲区（log cache buffer）的字节数。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG_BACKEND_ADSP_MTRACE && !CONFIG_LOG_FRONTEND_ONLY && !CONFIG_LOG_MODE_MINIMAL && CONFIG_LOG
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 32768]
```

**定义位置（Location）**：[`subsys/logging/backends/Kconfig.adsp_mtrace:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/backends/Kconfig.adsp_mtrace#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 日志（Logging）。 → 日志（Logging）。 → 后端（Backends） → Intel ADSP mtrace 后端

**配置项引用（Symbol References）**：[`CONFIG_LOG_BACKEND_ADSP_MTRACE`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG_BACKEND_ADSP_MTRACE)、[`CONFIG_LOG_FRONTEND_ONLY`](P368_subsys_logging_配置项参考_17.md#CONFIG_LOG_FRONTEND_ONLY)、[`CONFIG_LOG_MODE_MINIMAL`](P369_subsys_logging_配置项参考_18.md#CONFIG_LOG_MODE_MINIMAL)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_MUX_LOG_LEVEL_CHOICE"></a>

## 372.88 `CONFIG_MUX_LOG_LEVEL_CHOICE`

**提示（Prompt）**：多路复用器（mux）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MUX
```

**默认值（Defaults）**

```text
CONFIG_MUX_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MUX_LOG_LEVEL_OFF
CONFIG_MUX_LOG_LEVEL_ERR
CONFIG_MUX_LOG_LEVEL_WRN
CONFIG_MUX_LOG_LEVEL_INF
CONFIG_MUX_LOG_LEVEL_DBG
CONFIG_MUX_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多路复用器（Multiplexer，MUX）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MUX`](P130_drivers_mux_配置项参考.md#CONFIG_MUX)、[`CONFIG_MUX_LOG_LEVEL_DEFAULT`](P372_subsys_logging_配置项参考_21.md#CONFIG_MUX_LOG_LEVEL_DEFAULT)、[`CONFIG_MUX_LOG_LEVEL_OFF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MUX_LOG_LEVEL_OFF)、[`CONFIG_MUX_LOG_LEVEL_ERR`](P372_subsys_logging_配置项参考_21.md#CONFIG_MUX_LOG_LEVEL_ERR)、[`CONFIG_MUX_LOG_LEVEL_WRN`](P372_subsys_logging_配置项参考_21.md#CONFIG_MUX_LOG_LEVEL_WRN)、[`CONFIG_MUX_LOG_LEVEL_INF`](P372_subsys_logging_配置项参考_21.md#CONFIG_MUX_LOG_LEVEL_INF)、[`CONFIG_MUX_LOG_LEVEL_DBG`](P372_subsys_logging_配置项参考_21.md#CONFIG_MUX_LOG_LEVEL_DBG)。

<a id="CONFIG_MUX_LOG_LEVEL_DBG"></a>

## 372.89 `CONFIG_MUX_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MUX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多路复用器（Multiplexer，MUX）驱动 → 多路复用器（mux）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MUX_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MUX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MUX_LOG_LEVEL_DEFAULT"></a>

## 372.90 `CONFIG_MUX_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MUX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多路复用器（Multiplexer，MUX）驱动 → 多路复用器（mux）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MUX_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MUX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MUX_LOG_LEVEL_ERR"></a>

## 372.91 `CONFIG_MUX_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MUX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多路复用器（Multiplexer，MUX）驱动 → 多路复用器（mux）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MUX_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MUX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MUX_LOG_LEVEL_INF"></a>

## 372.92 `CONFIG_MUX_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MUX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多路复用器（Multiplexer，MUX）驱动 → 多路复用器（mux）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MUX_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MUX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MUX_LOG_LEVEL_OFF"></a>

## 372.93 `CONFIG_MUX_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MUX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多路复用器（Multiplexer，MUX）驱动 → 多路复用器（mux）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MUX_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MUX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MUX_LOG_LEVEL_WRN"></a>

## 372.94 `CONFIG_MUX_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MUX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多路复用器（Multiplexer，MUX）驱动 → 多路复用器（mux）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MUX_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_MUX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_BUF_LOG_LEVEL_CHOICE"></a>

## 372.95 `CONFIG_NET_BUF_LOG_LEVEL_CHOICE`

**提示（Prompt）**：网络缓冲区（net_buf）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_NET_BUF
```

**默认值（Defaults）**

```text
CONFIG_NET_BUF_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_BUF_LOG_LEVEL_OFF
CONFIG_NET_BUF_LOG_LEVEL_ERR
CONFIG_NET_BUF_LOG_LEVEL_WRN
CONFIG_NET_BUF_LOG_LEVEL_INF
CONFIG_NET_BUF_LOG_LEVEL_DBG
CONFIG_NET_BUF_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 网络缓冲区（Network buffer）支持

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_NET_BUF`](P198_lib_配置项参考_2.md#CONFIG_NET_BUF)、[`CONFIG_NET_BUF_LOG_LEVEL_DEFAULT`](P372_subsys_logging_配置项参考_21.md#CONFIG_NET_BUF_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_BUF_LOG_LEVEL_OFF`](P372_subsys_logging_配置项参考_21.md#CONFIG_NET_BUF_LOG_LEVEL_OFF)、[`CONFIG_NET_BUF_LOG_LEVEL_ERR`](P372_subsys_logging_配置项参考_21.md#CONFIG_NET_BUF_LOG_LEVEL_ERR)、[`CONFIG_NET_BUF_LOG_LEVEL_WRN`](P373_subsys_logging_配置项参考_22.md#CONFIG_NET_BUF_LOG_LEVEL_WRN)、[`CONFIG_NET_BUF_LOG_LEVEL_INF`](P372_subsys_logging_配置项参考_21.md#CONFIG_NET_BUF_LOG_LEVEL_INF)、[`CONFIG_NET_BUF_LOG_LEVEL_DBG`](P372_subsys_logging_配置项参考_21.md#CONFIG_NET_BUF_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_BUF_LOG_LEVEL_DBG"></a>

## 372.96 `CONFIG_NET_BUF_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_BUF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 网络缓冲区（Network buffer）支持 → 网络缓冲区（net_buf）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_BUF_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_NET_BUF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_BUF_LOG_LEVEL_DEFAULT"></a>

## 372.97 `CONFIG_NET_BUF_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_BUF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 网络缓冲区（Network buffer）支持 → 网络缓冲区（net_buf）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_BUF_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_NET_BUF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_BUF_LOG_LEVEL_ERR"></a>

## 372.98 `CONFIG_NET_BUF_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_BUF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 网络缓冲区（Network buffer）支持 → 网络缓冲区（net_buf）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_BUF_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_NET_BUF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_BUF_LOG_LEVEL_INF"></a>

## 372.99 `CONFIG_NET_BUF_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_BUF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 网络缓冲区（Network buffer）支持 → 网络缓冲区（net_buf）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_BUF_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_NET_BUF_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_BUF_LOG_LEVEL_OFF"></a>

## 372.100 `CONFIG_NET_BUF_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_BUF_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 附加库（Additional libraries） → 网络缓冲区（Network buffer）支持 → 网络缓冲区（net_buf）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_BUF_LOG_LEVEL_CHOICE`](P372_subsys_logging_配置项参考_21.md#CONFIG_NET_BUF_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P371_subsys_logging_配置项参考_20.md) · [返回大纲](大纲.md) · [下一章](P373_subsys_logging_配置项参考_22.md)
