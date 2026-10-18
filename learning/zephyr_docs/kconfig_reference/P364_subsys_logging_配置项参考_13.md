---
id: learning.zephyr-docs.kconfig-reference.page-364
title: "`subsys/logging`配置项参考（13/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第364章\_`subsys/logging`配置项参考（13/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_FLASH_LOG_LEVEL_INF"></a>

## 364.1 `CONFIG_FLASH_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FLASH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 闪存（flash）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_FLASH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FLASH_LOG_LEVEL_OFF"></a>

## 364.2 `CONFIG_FLASH_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FLASH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 闪存（flash）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_FLASH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FLASH_LOG_LEVEL_WRN"></a>

## 364.3 `CONFIG_FLASH_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FLASH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 闪存（flash）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_FLASH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FOTA_HTTP_LOG_LEVEL_CHOICE"></a>

## 364.4 `CONFIG_FOTA_HTTP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：通过 HTTP 的固件空中更新（fota_http）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_FOTA_HTTP
```

**默认值（Defaults）**

```text
CONFIG_FOTA_HTTP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_FOTA_HTTP_LOG_LEVEL_OFF
CONFIG_FOTA_HTTP_LOG_LEVEL_ERR
CONFIG_FOTA_HTTP_LOG_LEVEL_WRN
CONFIG_FOTA_HTTP_LOG_LEVEL_INF
CONFIG_FOTA_HTTP_LOG_LEVEL_DBG
CONFIG_FOTA_HTTP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 基于HTTP的固件空中升级（Firmware Over-the-Air）。

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_FOTA_HTTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FOTA_HTTP)、[`CONFIG_FOTA_HTTP_LOG_LEVEL_DEFAULT`](P364_subsys_logging_配置项参考_13.md#CONFIG_FOTA_HTTP_LOG_LEVEL_DEFAULT)、[`CONFIG_FOTA_HTTP_LOG_LEVEL_OFF`](P364_subsys_logging_配置项参考_13.md#CONFIG_FOTA_HTTP_LOG_LEVEL_OFF)、[`CONFIG_FOTA_HTTP_LOG_LEVEL_ERR`](P364_subsys_logging_配置项参考_13.md#CONFIG_FOTA_HTTP_LOG_LEVEL_ERR)、[`CONFIG_FOTA_HTTP_LOG_LEVEL_WRN`](P364_subsys_logging_配置项参考_13.md#CONFIG_FOTA_HTTP_LOG_LEVEL_WRN)、[`CONFIG_FOTA_HTTP_LOG_LEVEL_INF`](P364_subsys_logging_配置项参考_13.md#CONFIG_FOTA_HTTP_LOG_LEVEL_INF)、[`CONFIG_FOTA_HTTP_LOG_LEVEL_DBG`](P364_subsys_logging_配置项参考_13.md#CONFIG_FOTA_HTTP_LOG_LEVEL_DBG)。

<a id="CONFIG_FOTA_HTTP_LOG_LEVEL_DBG"></a>

## 364.5 `CONFIG_FOTA_HTTP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FOTA_HTTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 基于HTTP的固件空中升级（Firmware Over-the-Air）。 → 通过 HTTP 的固件空中更新（fota_http）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FOTA_HTTP_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FOTA_HTTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FOTA_HTTP_LOG_LEVEL_DEFAULT"></a>

## 364.6 `CONFIG_FOTA_HTTP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FOTA_HTTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 基于HTTP的固件空中升级（Firmware Over-the-Air）。 → 通过 HTTP 的固件空中更新（fota_http）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FOTA_HTTP_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FOTA_HTTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FOTA_HTTP_LOG_LEVEL_ERR"></a>

## 364.7 `CONFIG_FOTA_HTTP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FOTA_HTTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 基于HTTP的固件空中升级（Firmware Over-the-Air）。 → 通过 HTTP 的固件空中更新（fota_http）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FOTA_HTTP_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FOTA_HTTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FOTA_HTTP_LOG_LEVEL_INF"></a>

## 364.8 `CONFIG_FOTA_HTTP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FOTA_HTTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 基于HTTP的固件空中升级（Firmware Over-the-Air）。 → 通过 HTTP 的固件空中更新（fota_http）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FOTA_HTTP_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FOTA_HTTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FOTA_HTTP_LOG_LEVEL_OFF"></a>

## 364.9 `CONFIG_FOTA_HTTP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FOTA_HTTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 基于HTTP的固件空中升级（Firmware Over-the-Air）。 → 通过 HTTP 的固件空中更新（fota_http）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FOTA_HTTP_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FOTA_HTTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FOTA_HTTP_LOG_LEVEL_WRN"></a>

## 364.10 `CONFIG_FOTA_HTTP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FOTA_HTTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 基于HTTP的固件空中升级（Firmware Over-the-Air）。 → 通过 HTTP 的固件空中更新（fota_http）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FOTA_HTTP_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FOTA_HTTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FPGA_LOG_LEVEL_CHOICE"></a>

## 364.11 `CONFIG_FPGA_LOG_LEVEL_CHOICE`

**提示（Prompt）**：现场可编程门阵列（fpga）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_FPGA
```

**默认值（Defaults）**

```text
CONFIG_FPGA_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_FPGA_LOG_LEVEL_OFF
CONFIG_FPGA_LOG_LEVEL_ERR
CONFIG_FPGA_LOG_LEVEL_WRN
CONFIG_FPGA_LOG_LEVEL_INF
CONFIG_FPGA_LOG_LEVEL_DBG
CONFIG_FPGA_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 现场可编程门阵列（Field-Programmable Gate Array，FPGA）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_FPGA`](P095_drivers_fpga_配置项参考.md#CONFIG_FPGA)、[`CONFIG_FPGA_LOG_LEVEL_DEFAULT`](P364_subsys_logging_配置项参考_13.md#CONFIG_FPGA_LOG_LEVEL_DEFAULT)、[`CONFIG_FPGA_LOG_LEVEL_OFF`](P364_subsys_logging_配置项参考_13.md#CONFIG_FPGA_LOG_LEVEL_OFF)、[`CONFIG_FPGA_LOG_LEVEL_ERR`](P364_subsys_logging_配置项参考_13.md#CONFIG_FPGA_LOG_LEVEL_ERR)、[`CONFIG_FPGA_LOG_LEVEL_WRN`](P364_subsys_logging_配置项参考_13.md#CONFIG_FPGA_LOG_LEVEL_WRN)、[`CONFIG_FPGA_LOG_LEVEL_INF`](P364_subsys_logging_配置项参考_13.md#CONFIG_FPGA_LOG_LEVEL_INF)、[`CONFIG_FPGA_LOG_LEVEL_DBG`](P364_subsys_logging_配置项参考_13.md#CONFIG_FPGA_LOG_LEVEL_DBG)。

<a id="CONFIG_FPGA_LOG_LEVEL_DBG"></a>

## 364.12 `CONFIG_FPGA_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FPGA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 现场可编程门阵列（Field-Programmable Gate Array，FPGA）驱动 → 现场可编程门阵列（fpga）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FPGA_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FPGA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FPGA_LOG_LEVEL_DEFAULT"></a>

## 364.13 `CONFIG_FPGA_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FPGA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 现场可编程门阵列（Field-Programmable Gate Array，FPGA）驱动 → 现场可编程门阵列（fpga）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FPGA_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FPGA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FPGA_LOG_LEVEL_ERR"></a>

## 364.14 `CONFIG_FPGA_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FPGA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 现场可编程门阵列（Field-Programmable Gate Array，FPGA）驱动 → 现场可编程门阵列（fpga）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FPGA_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FPGA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FPGA_LOG_LEVEL_INF"></a>

## 364.15 `CONFIG_FPGA_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FPGA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 现场可编程门阵列（Field-Programmable Gate Array，FPGA）驱动 → 现场可编程门阵列（fpga）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FPGA_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FPGA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FPGA_LOG_LEVEL_OFF"></a>

## 364.16 `CONFIG_FPGA_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FPGA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 现场可编程门阵列（Field-Programmable Gate Array，FPGA）驱动 → 现场可编程门阵列（fpga）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FPGA_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FPGA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FPGA_LOG_LEVEL_WRN"></a>

## 364.17 `CONFIG_FPGA_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FPGA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 现场可编程门阵列（Field-Programmable Gate Array，FPGA）驱动 → 现场可编程门阵列（fpga）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FPGA_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FPGA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FS_LOG_LEVEL_CHOICE"></a>

## 364.18 `CONFIG_FS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：文件系统（fs）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
CONFIG_FS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_FS_LOG_LEVEL_OFF
CONFIG_FS_LOG_LEVEL_ERR
CONFIG_FS_LOG_LEVEL_WRN
CONFIG_FS_LOG_LEVEL_INF
CONFIG_FS_LOG_LEVEL_DBG
CONFIG_FS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)、[`CONFIG_FS_LOG_LEVEL_DEFAULT`](P364_subsys_logging_配置项参考_13.md#CONFIG_FS_LOG_LEVEL_DEFAULT)、[`CONFIG_FS_LOG_LEVEL_OFF`](P364_subsys_logging_配置项参考_13.md#CONFIG_FS_LOG_LEVEL_OFF)、[`CONFIG_FS_LOG_LEVEL_ERR`](P364_subsys_logging_配置项参考_13.md#CONFIG_FS_LOG_LEVEL_ERR)、[`CONFIG_FS_LOG_LEVEL_WRN`](P364_subsys_logging_配置项参考_13.md#CONFIG_FS_LOG_LEVEL_WRN)、[`CONFIG_FS_LOG_LEVEL_INF`](P364_subsys_logging_配置项参考_13.md#CONFIG_FS_LOG_LEVEL_INF)、[`CONFIG_FS_LOG_LEVEL_DBG`](P364_subsys_logging_配置项参考_13.md#CONFIG_FS_LOG_LEVEL_DBG)。

<a id="CONFIG_FS_LOG_LEVEL_DBG"></a>

## 364.19 `CONFIG_FS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 文件系统（fs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FS_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FS_LOG_LEVEL_DEFAULT"></a>

## 364.20 `CONFIG_FS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 文件系统（fs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FS_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FS_LOG_LEVEL_ERR"></a>

## 364.21 `CONFIG_FS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 文件系统（fs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FS_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FS_LOG_LEVEL_INF"></a>

## 364.22 `CONFIG_FS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 文件系统（fs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FS_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FS_LOG_LEVEL_OFF"></a>

## 364.23 `CONFIG_FS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 文件系统（fs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FS_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FS_LOG_LEVEL_WRN"></a>

## 364.24 `CONFIG_FS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 文件系统（fs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FS_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FTP_CLIENT_LOG_LEVEL_CHOICE"></a>

## 364.25 `CONFIG_FTP_CLIENT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：文件传输协议客户端（FTP client）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_FTP_CLIENT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_FTP_CLIENT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_FTP_CLIENT_LOG_LEVEL_OFF
CONFIG_FTP_CLIENT_LOG_LEVEL_ERR
CONFIG_FTP_CLIENT_LOG_LEVEL_WRN
CONFIG_FTP_CLIENT_LOG_LEVEL_INF
CONFIG_FTP_CLIENT_LOG_LEVEL_DBG
CONFIG_FTP_CLIENT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 文件传输协议客户端（FTP client）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_FTP_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_FTP_CLIENT)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_FTP_CLIENT_LOG_LEVEL_DEFAULT`](P364_subsys_logging_配置项参考_13.md#CONFIG_FTP_CLIENT_LOG_LEVEL_DEFAULT)、[`CONFIG_FTP_CLIENT_LOG_LEVEL_OFF`](P364_subsys_logging_配置项参考_13.md#CONFIG_FTP_CLIENT_LOG_LEVEL_OFF)、[`CONFIG_FTP_CLIENT_LOG_LEVEL_ERR`](P364_subsys_logging_配置项参考_13.md#CONFIG_FTP_CLIENT_LOG_LEVEL_ERR)、[`CONFIG_FTP_CLIENT_LOG_LEVEL_WRN`](P364_subsys_logging_配置项参考_13.md#CONFIG_FTP_CLIENT_LOG_LEVEL_WRN)、[`CONFIG_FTP_CLIENT_LOG_LEVEL_INF`](P364_subsys_logging_配置项参考_13.md#CONFIG_FTP_CLIENT_LOG_LEVEL_INF)、[`CONFIG_FTP_CLIENT_LOG_LEVEL_DBG`](P364_subsys_logging_配置项参考_13.md#CONFIG_FTP_CLIENT_LOG_LEVEL_DBG)。

<a id="CONFIG_FTP_CLIENT_LOG_LEVEL_DBG"></a>

## 364.26 `CONFIG_FTP_CLIENT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FTP_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 文件传输协议客户端（FTP client）【实验性 EXPERIMENTAL】 → 文件传输协议客户端（FTP client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FTP_CLIENT_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FTP_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FTP_CLIENT_LOG_LEVEL_DEFAULT"></a>

## 364.27 `CONFIG_FTP_CLIENT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FTP_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 文件传输协议客户端（FTP client）【实验性 EXPERIMENTAL】 → 文件传输协议客户端（FTP client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FTP_CLIENT_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FTP_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FTP_CLIENT_LOG_LEVEL_ERR"></a>

## 364.28 `CONFIG_FTP_CLIENT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FTP_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 文件传输协议客户端（FTP client）【实验性 EXPERIMENTAL】 → 文件传输协议客户端（FTP client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FTP_CLIENT_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FTP_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FTP_CLIENT_LOG_LEVEL_INF"></a>

## 364.29 `CONFIG_FTP_CLIENT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FTP_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 文件传输协议客户端（FTP client）【实验性 EXPERIMENTAL】 → 文件传输协议客户端（FTP client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FTP_CLIENT_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FTP_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FTP_CLIENT_LOG_LEVEL_OFF"></a>

## 364.30 `CONFIG_FTP_CLIENT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FTP_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 文件传输协议客户端（FTP client）【实验性 EXPERIMENTAL】 → 文件传输协议客户端（FTP client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FTP_CLIENT_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FTP_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FTP_CLIENT_LOG_LEVEL_WRN"></a>

## 364.31 `CONFIG_FTP_CLIENT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FTP_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 文件传输协议客户端（FTP client）【实验性 EXPERIMENTAL】 → 文件传输协议客户端（FTP client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FTP_CLIENT_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FTP_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FUEL_GAUGE_LOG_LEVEL_CHOICE"></a>

## 364.32 `CONFIG_FUEL_GAUGE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：电量计（fuel_gauge）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_FUEL_GAUGE
```

**默认值（Defaults）**

```text
CONFIG_FUEL_GAUGE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_FUEL_GAUGE_LOG_LEVEL_OFF
CONFIG_FUEL_GAUGE_LOG_LEVEL_ERR
CONFIG_FUEL_GAUGE_LOG_LEVEL_WRN
CONFIG_FUEL_GAUGE_LOG_LEVEL_INF
CONFIG_FUEL_GAUGE_LOG_LEVEL_DBG
CONFIG_FUEL_GAUGE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_FUEL_GAUGE`](P096_drivers_fuel_gauge_配置项参考.md#CONFIG_FUEL_GAUGE)、[`CONFIG_FUEL_GAUGE_LOG_LEVEL_DEFAULT`](P364_subsys_logging_配置项参考_13.md#CONFIG_FUEL_GAUGE_LOG_LEVEL_DEFAULT)、[`CONFIG_FUEL_GAUGE_LOG_LEVEL_OFF`](P364_subsys_logging_配置项参考_13.md#CONFIG_FUEL_GAUGE_LOG_LEVEL_OFF)、[`CONFIG_FUEL_GAUGE_LOG_LEVEL_ERR`](P364_subsys_logging_配置项参考_13.md#CONFIG_FUEL_GAUGE_LOG_LEVEL_ERR)、[`CONFIG_FUEL_GAUGE_LOG_LEVEL_WRN`](P364_subsys_logging_配置项参考_13.md#CONFIG_FUEL_GAUGE_LOG_LEVEL_WRN)、[`CONFIG_FUEL_GAUGE_LOG_LEVEL_INF`](P364_subsys_logging_配置项参考_13.md#CONFIG_FUEL_GAUGE_LOG_LEVEL_INF)、[`CONFIG_FUEL_GAUGE_LOG_LEVEL_DBG`](P364_subsys_logging_配置项参考_13.md#CONFIG_FUEL_GAUGE_LOG_LEVEL_DBG)。

<a id="CONFIG_FUEL_GAUGE_LOG_LEVEL_DBG"></a>

## 364.33 `CONFIG_FUEL_GAUGE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FUEL_GAUGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers） → 电量计（fuel_gauge）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FUEL_GAUGE_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FUEL_GAUGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FUEL_GAUGE_LOG_LEVEL_DEFAULT"></a>

## 364.34 `CONFIG_FUEL_GAUGE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FUEL_GAUGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers） → 电量计（fuel_gauge）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FUEL_GAUGE_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FUEL_GAUGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FUEL_GAUGE_LOG_LEVEL_ERR"></a>

## 364.35 `CONFIG_FUEL_GAUGE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FUEL_GAUGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers） → 电量计（fuel_gauge）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FUEL_GAUGE_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FUEL_GAUGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FUEL_GAUGE_LOG_LEVEL_INF"></a>

## 364.36 `CONFIG_FUEL_GAUGE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FUEL_GAUGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers） → 电量计（fuel_gauge）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FUEL_GAUGE_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FUEL_GAUGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FUEL_GAUGE_LOG_LEVEL_OFF"></a>

## 364.37 `CONFIG_FUEL_GAUGE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FUEL_GAUGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers） → 电量计（fuel_gauge）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FUEL_GAUGE_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FUEL_GAUGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FUEL_GAUGE_LOG_LEVEL_WRN"></a>

## 364.38 `CONFIG_FUEL_GAUGE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FUEL_GAUGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电池电量计驱动（Battery Fuel Gauge Drivers） → 电量计（fuel_gauge）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FUEL_GAUGE_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FUEL_GAUGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FUSE_CLIENT_LOG_LEVEL_CHOICE"></a>

## 364.39 `CONFIG_FUSE_CLIENT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：用户空间文件系统（fuse）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
CONFIG_FUSE_CLIENT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_FUSE_CLIENT_LOG_LEVEL_OFF
CONFIG_FUSE_CLIENT_LOG_LEVEL_ERR
CONFIG_FUSE_CLIENT_LOG_LEVEL_WRN
CONFIG_FUSE_CLIENT_LOG_LEVEL_INF
CONFIG_FUSE_CLIENT_LOG_LEVEL_DBG
CONFIG_FUSE_CLIENT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)、[`CONFIG_FUSE_CLIENT_LOG_LEVEL_DEFAULT`](P364_subsys_logging_配置项参考_13.md#CONFIG_FUSE_CLIENT_LOG_LEVEL_DEFAULT)、[`CONFIG_FUSE_CLIENT_LOG_LEVEL_OFF`](P364_subsys_logging_配置项参考_13.md#CONFIG_FUSE_CLIENT_LOG_LEVEL_OFF)、[`CONFIG_FUSE_CLIENT_LOG_LEVEL_ERR`](P364_subsys_logging_配置项参考_13.md#CONFIG_FUSE_CLIENT_LOG_LEVEL_ERR)、[`CONFIG_FUSE_CLIENT_LOG_LEVEL_WRN`](P364_subsys_logging_配置项参考_13.md#CONFIG_FUSE_CLIENT_LOG_LEVEL_WRN)、[`CONFIG_FUSE_CLIENT_LOG_LEVEL_INF`](P364_subsys_logging_配置项参考_13.md#CONFIG_FUSE_CLIENT_LOG_LEVEL_INF)、[`CONFIG_FUSE_CLIENT_LOG_LEVEL_DBG`](P364_subsys_logging_配置项参考_13.md#CONFIG_FUSE_CLIENT_LOG_LEVEL_DBG)。

<a id="CONFIG_FUSE_CLIENT_LOG_LEVEL_DBG"></a>

## 364.40 `CONFIG_FUSE_CLIENT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FUSE_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 用户空间文件系统（fuse）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FUSE_CLIENT_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FUSE_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FUSE_CLIENT_LOG_LEVEL_DEFAULT"></a>

## 364.41 `CONFIG_FUSE_CLIENT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FUSE_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 用户空间文件系统（fuse）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FUSE_CLIENT_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FUSE_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FUSE_CLIENT_LOG_LEVEL_ERR"></a>

## 364.42 `CONFIG_FUSE_CLIENT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FUSE_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 用户空间文件系统（fuse）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FUSE_CLIENT_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FUSE_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FUSE_CLIENT_LOG_LEVEL_INF"></a>

## 364.43 `CONFIG_FUSE_CLIENT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FUSE_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 用户空间文件系统（fuse）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FUSE_CLIENT_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FUSE_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FUSE_CLIENT_LOG_LEVEL_OFF"></a>

## 364.44 `CONFIG_FUSE_CLIENT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FUSE_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 用户空间文件系统（fuse）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FUSE_CLIENT_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FUSE_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FUSE_CLIENT_LOG_LEVEL_WRN"></a>

## 364.45 `CONFIG_FUSE_CLIENT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FUSE_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → 用户空间文件系统（fuse）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FUSE_CLIENT_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FUSE_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FXL6408_LOG_LEVEL_CHOICE"></a>

## 364.46 `CONFIG_FXL6408_LOG_LEVEL_CHOICE`

**提示（Prompt）**：FXL6408 驱动（fxl6408）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_GPIO_FXL6408 && CONFIG_GPIO
```

**默认值（Defaults）**

```text
CONFIG_FXL6408_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_FXL6408_LOG_LEVEL_OFF
CONFIG_FXL6408_LOG_LEVEL_ERR
CONFIG_FXL6408_LOG_LEVEL_WRN
CONFIG_FXL6408_LOG_LEVEL_INF
CONFIG_FXL6408_LOG_LEVEL_DBG
CONFIG_FXL6408_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 基于 I2C 的 FXL6408 GPIO 芯片

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_GPIO_FXL6408`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO_FXL6408)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_FXL6408_LOG_LEVEL_DEFAULT`](P364_subsys_logging_配置项参考_13.md#CONFIG_FXL6408_LOG_LEVEL_DEFAULT)、[`CONFIG_FXL6408_LOG_LEVEL_OFF`](P364_subsys_logging_配置项参考_13.md#CONFIG_FXL6408_LOG_LEVEL_OFF)、[`CONFIG_FXL6408_LOG_LEVEL_ERR`](P364_subsys_logging_配置项参考_13.md#CONFIG_FXL6408_LOG_LEVEL_ERR)、[`CONFIG_FXL6408_LOG_LEVEL_WRN`](P364_subsys_logging_配置项参考_13.md#CONFIG_FXL6408_LOG_LEVEL_WRN)、[`CONFIG_FXL6408_LOG_LEVEL_INF`](P364_subsys_logging_配置项参考_13.md#CONFIG_FXL6408_LOG_LEVEL_INF)、[`CONFIG_FXL6408_LOG_LEVEL_DBG`](P364_subsys_logging_配置项参考_13.md#CONFIG_FXL6408_LOG_LEVEL_DBG)。

<a id="CONFIG_FXL6408_LOG_LEVEL_DBG"></a>

## 364.47 `CONFIG_FXL6408_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FXL6408_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 基于 I2C 的 FXL6408 GPIO 芯片 → FXL6408 驱动（fxl6408）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FXL6408_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FXL6408_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FXL6408_LOG_LEVEL_DEFAULT"></a>

## 364.48 `CONFIG_FXL6408_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FXL6408_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 基于 I2C 的 FXL6408 GPIO 芯片 → FXL6408 驱动（fxl6408）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FXL6408_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FXL6408_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FXL6408_LOG_LEVEL_ERR"></a>

## 364.49 `CONFIG_FXL6408_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FXL6408_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 基于 I2C 的 FXL6408 GPIO 芯片 → FXL6408 驱动（fxl6408）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FXL6408_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FXL6408_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FXL6408_LOG_LEVEL_INF"></a>

## 364.50 `CONFIG_FXL6408_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FXL6408_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 基于 I2C 的 FXL6408 GPIO 芯片 → FXL6408 驱动（fxl6408）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FXL6408_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FXL6408_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FXL6408_LOG_LEVEL_OFF"></a>

## 364.51 `CONFIG_FXL6408_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FXL6408_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 基于 I2C 的 FXL6408 GPIO 芯片 → FXL6408 驱动（fxl6408）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FXL6408_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FXL6408_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FXL6408_LOG_LEVEL_WRN"></a>

## 364.52 `CONFIG_FXL6408_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FXL6408_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 基于 I2C 的 FXL6408 GPIO 芯片 → FXL6408 驱动（fxl6408）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FXL6408_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_FXL6408_LOG_LEVEL_CHOICE)。

<a id="CONFIG_GNSS_LOG_LEVEL_CHOICE"></a>

## 364.53 `CONFIG_GNSS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：全球导航卫星系统（gnss）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_GNSS
```

**默认值（Defaults）**

```text
CONFIG_GNSS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_GNSS_LOG_LEVEL_OFF
CONFIG_GNSS_LOG_LEVEL_ERR
CONFIG_GNSS_LOG_LEVEL_WRN
CONFIG_GNSS_LOG_LEVEL_INF
CONFIG_GNSS_LOG_LEVEL_DBG
CONFIG_GNSS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_GNSS`](P097_drivers_gnss_配置项参考.md#CONFIG_GNSS)、[`CONFIG_GNSS_LOG_LEVEL_DEFAULT`](P364_subsys_logging_配置项参考_13.md#CONFIG_GNSS_LOG_LEVEL_DEFAULT)、[`CONFIG_GNSS_LOG_LEVEL_OFF`](P364_subsys_logging_配置项参考_13.md#CONFIG_GNSS_LOG_LEVEL_OFF)、[`CONFIG_GNSS_LOG_LEVEL_ERR`](P364_subsys_logging_配置项参考_13.md#CONFIG_GNSS_LOG_LEVEL_ERR)、[`CONFIG_GNSS_LOG_LEVEL_WRN`](P364_subsys_logging_配置项参考_13.md#CONFIG_GNSS_LOG_LEVEL_WRN)、[`CONFIG_GNSS_LOG_LEVEL_INF`](P364_subsys_logging_配置项参考_13.md#CONFIG_GNSS_LOG_LEVEL_INF)、[`CONFIG_GNSS_LOG_LEVEL_DBG`](P364_subsys_logging_配置项参考_13.md#CONFIG_GNSS_LOG_LEVEL_DBG)。

<a id="CONFIG_GNSS_LOG_LEVEL_DBG"></a>

## 364.54 `CONFIG_GNSS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GNSS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → 全球导航卫星系统（gnss）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_GNSS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_GNSS_LOG_LEVEL_DEFAULT"></a>

## 364.55 `CONFIG_GNSS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GNSS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → 全球导航卫星系统（gnss）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_GNSS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_GNSS_LOG_LEVEL_ERR"></a>

## 364.56 `CONFIG_GNSS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GNSS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → 全球导航卫星系统（gnss）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_GNSS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_GNSS_LOG_LEVEL_INF"></a>

## 364.57 `CONFIG_GNSS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GNSS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → 全球导航卫星系统（gnss）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_GNSS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_GNSS_LOG_LEVEL_OFF"></a>

## 364.58 `CONFIG_GNSS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GNSS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → 全球导航卫星系统（gnss）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_GNSS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_GNSS_LOG_LEVEL_WRN"></a>

## 364.59 `CONFIG_GNSS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GNSS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 全球导航卫星系统（Global Navigation Satellite System，GNSS）驱动【实验性】 → 全球导航卫星系统（gnss）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_GNSS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_GNSS_RTK_LOG_LEVEL_CHOICE"></a>

## 364.60 `CONFIG_GNSS_RTK_LOG_LEVEL_CHOICE`

**提示（Prompt）**：全球导航卫星系统实时动态差分（GNSS RTK）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_GNSS_RTK
```

**默认值（Defaults）**

```text
CONFIG_GNSS_RTK_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_GNSS_RTK_LOG_LEVEL_OFF
CONFIG_GNSS_RTK_LOG_LEVEL_ERR
CONFIG_GNSS_RTK_LOG_LEVEL_WRN
CONFIG_GNSS_RTK_LOG_LEVEL_INF
CONFIG_GNSS_RTK_LOG_LEVEL_DBG
CONFIG_GNSS_RTK_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 全球导航卫星系统实时动态差分客户端（GNSS RTK client）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_GNSS_RTK`](P345_subsys_gnss_配置项参考.md#CONFIG_GNSS_RTK)、[`CONFIG_GNSS_RTK_LOG_LEVEL_DEFAULT`](P364_subsys_logging_配置项参考_13.md#CONFIG_GNSS_RTK_LOG_LEVEL_DEFAULT)、[`CONFIG_GNSS_RTK_LOG_LEVEL_OFF`](P364_subsys_logging_配置项参考_13.md#CONFIG_GNSS_RTK_LOG_LEVEL_OFF)、[`CONFIG_GNSS_RTK_LOG_LEVEL_ERR`](P364_subsys_logging_配置项参考_13.md#CONFIG_GNSS_RTK_LOG_LEVEL_ERR)、[`CONFIG_GNSS_RTK_LOG_LEVEL_WRN`](P364_subsys_logging_配置项参考_13.md#CONFIG_GNSS_RTK_LOG_LEVEL_WRN)、[`CONFIG_GNSS_RTK_LOG_LEVEL_INF`](P364_subsys_logging_配置项参考_13.md#CONFIG_GNSS_RTK_LOG_LEVEL_INF)、[`CONFIG_GNSS_RTK_LOG_LEVEL_DBG`](P364_subsys_logging_配置项参考_13.md#CONFIG_GNSS_RTK_LOG_LEVEL_DBG)。

<a id="CONFIG_GNSS_RTK_LOG_LEVEL_DBG"></a>

## 364.61 `CONFIG_GNSS_RTK_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GNSS_RTK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 全球导航卫星系统实时动态差分客户端（GNSS RTK client）【实验性 EXPERIMENTAL】 → 全球导航卫星系统实时动态差分（GNSS RTK）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_RTK_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_GNSS_RTK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_GNSS_RTK_LOG_LEVEL_DEFAULT"></a>

## 364.62 `CONFIG_GNSS_RTK_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GNSS_RTK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 全球导航卫星系统实时动态差分客户端（GNSS RTK client）【实验性 EXPERIMENTAL】 → 全球导航卫星系统实时动态差分（GNSS RTK）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_RTK_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_GNSS_RTK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_GNSS_RTK_LOG_LEVEL_ERR"></a>

## 364.63 `CONFIG_GNSS_RTK_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GNSS_RTK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 全球导航卫星系统实时动态差分客户端（GNSS RTK client）【实验性 EXPERIMENTAL】 → 全球导航卫星系统实时动态差分（GNSS RTK）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_RTK_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_GNSS_RTK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_GNSS_RTK_LOG_LEVEL_INF"></a>

## 364.64 `CONFIG_GNSS_RTK_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GNSS_RTK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 全球导航卫星系统实时动态差分客户端（GNSS RTK client）【实验性 EXPERIMENTAL】 → 全球导航卫星系统实时动态差分（GNSS RTK）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_RTK_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_GNSS_RTK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_GNSS_RTK_LOG_LEVEL_OFF"></a>

## 364.65 `CONFIG_GNSS_RTK_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GNSS_RTK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 全球导航卫星系统实时动态差分客户端（GNSS RTK client）【实验性 EXPERIMENTAL】 → 全球导航卫星系统实时动态差分（GNSS RTK）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_RTK_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_GNSS_RTK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_GNSS_RTK_LOG_LEVEL_WRN"></a>

## 364.66 `CONFIG_GNSS_RTK_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GNSS_RTK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 全球导航卫星系统实时动态差分客户端（GNSS RTK client）【实验性 EXPERIMENTAL】 → 全球导航卫星系统实时动态差分（GNSS RTK）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_GNSS_RTK_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_GNSS_RTK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_GPIO_LOG_LEVEL_CHOICE"></a>

## 364.67 `CONFIG_GPIO_LOG_LEVEL_CHOICE`

**提示（Prompt）**：通用输入输出（gpio）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_GPIO
```

**默认值（Defaults）**

```text
CONFIG_GPIO_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_GPIO_LOG_LEVEL_OFF
CONFIG_GPIO_LOG_LEVEL_ERR
CONFIG_GPIO_LOG_LEVEL_WRN
CONFIG_GPIO_LOG_LEVEL_INF
CONFIG_GPIO_LOG_LEVEL_DBG
CONFIG_GPIO_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_GPIO`](P098_drivers_gpio_配置项参考_1.md#CONFIG_GPIO)、[`CONFIG_GPIO_LOG_LEVEL_DEFAULT`](P364_subsys_logging_配置项参考_13.md#CONFIG_GPIO_LOG_LEVEL_DEFAULT)、[`CONFIG_GPIO_LOG_LEVEL_OFF`](P364_subsys_logging_配置项参考_13.md#CONFIG_GPIO_LOG_LEVEL_OFF)、[`CONFIG_GPIO_LOG_LEVEL_ERR`](P364_subsys_logging_配置项参考_13.md#CONFIG_GPIO_LOG_LEVEL_ERR)、[`CONFIG_GPIO_LOG_LEVEL_WRN`](P364_subsys_logging_配置项参考_13.md#CONFIG_GPIO_LOG_LEVEL_WRN)、[`CONFIG_GPIO_LOG_LEVEL_INF`](P364_subsys_logging_配置项参考_13.md#CONFIG_GPIO_LOG_LEVEL_INF)、[`CONFIG_GPIO_LOG_LEVEL_DBG`](P364_subsys_logging_配置项参考_13.md#CONFIG_GPIO_LOG_LEVEL_DBG)。

<a id="CONFIG_GPIO_LOG_LEVEL_DBG"></a>

## 364.68 `CONFIG_GPIO_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GPIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 通用输入输出（gpio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_GPIO_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_GPIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_GPIO_LOG_LEVEL_DEFAULT"></a>

## 364.69 `CONFIG_GPIO_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GPIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 通用输入输出（gpio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_GPIO_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_GPIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_GPIO_LOG_LEVEL_ERR"></a>

## 364.70 `CONFIG_GPIO_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GPIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 通用输入输出（gpio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_GPIO_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_GPIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_GPIO_LOG_LEVEL_INF"></a>

## 364.71 `CONFIG_GPIO_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GPIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 通用输入输出（gpio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_GPIO_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_GPIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_GPIO_LOG_LEVEL_OFF"></a>

## 364.72 `CONFIG_GPIO_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GPIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 通用输入输出（gpio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_GPIO_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_GPIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_GPIO_LOG_LEVEL_WRN"></a>

## 364.73 `CONFIG_GPIO_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GPIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 通用输入/输出（General-Purpose Input/Output，GPIO）驱动 → 通用输入输出（gpio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_GPIO_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_GPIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_GROVE_LCD_RGB_LOG_LEVEL_CHOICE"></a>

## 364.74 `CONFIG_GROVE_LCD_RGB_LOG_LEVEL_CHOICE`

**提示（Prompt）**：Grove RGB 液晶显示屏（grove_lcd_rgb）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_GROVE_LCD_RGB
```

**默认值（Defaults）**

```text
CONFIG_GROVE_LCD_RGB_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_GROVE_LCD_RGB_LOG_LEVEL_OFF
CONFIG_GROVE_LCD_RGB_LOG_LEVEL_ERR
CONFIG_GROVE_LCD_RGB_LOG_LEVEL_WRN
CONFIG_GROVE_LCD_RGB_LOG_LEVEL_INF
CONFIG_GROVE_LCD_RGB_LOG_LEVEL_DBG
CONFIG_GROVE_LCD_RGB_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Seeed Grove LCD RGB 背光（Backlight）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_GROVE_LCD_RGB`](P123_drivers_misc_配置项参考.md#CONFIG_GROVE_LCD_RGB)、[`CONFIG_GROVE_LCD_RGB_LOG_LEVEL_DEFAULT`](P364_subsys_logging_配置项参考_13.md#CONFIG_GROVE_LCD_RGB_LOG_LEVEL_DEFAULT)、[`CONFIG_GROVE_LCD_RGB_LOG_LEVEL_OFF`](P364_subsys_logging_配置项参考_13.md#CONFIG_GROVE_LCD_RGB_LOG_LEVEL_OFF)、[`CONFIG_GROVE_LCD_RGB_LOG_LEVEL_ERR`](P364_subsys_logging_配置项参考_13.md#CONFIG_GROVE_LCD_RGB_LOG_LEVEL_ERR)、[`CONFIG_GROVE_LCD_RGB_LOG_LEVEL_WRN`](P364_subsys_logging_配置项参考_13.md#CONFIG_GROVE_LCD_RGB_LOG_LEVEL_WRN)、[`CONFIG_GROVE_LCD_RGB_LOG_LEVEL_INF`](P364_subsys_logging_配置项参考_13.md#CONFIG_GROVE_LCD_RGB_LOG_LEVEL_INF)、[`CONFIG_GROVE_LCD_RGB_LOG_LEVEL_DBG`](P364_subsys_logging_配置项参考_13.md#CONFIG_GROVE_LCD_RGB_LOG_LEVEL_DBG)。

<a id="CONFIG_GROVE_LCD_RGB_LOG_LEVEL_DBG"></a>

## 364.75 `CONFIG_GROVE_LCD_RGB_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GROVE_LCD_RGB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Seeed Grove LCD RGB 背光（Backlight） → Grove RGB 液晶显示屏（grove_lcd_rgb）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_GROVE_LCD_RGB_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_GROVE_LCD_RGB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_GROVE_LCD_RGB_LOG_LEVEL_DEFAULT"></a>

## 364.76 `CONFIG_GROVE_LCD_RGB_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GROVE_LCD_RGB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Seeed Grove LCD RGB 背光（Backlight） → Grove RGB 液晶显示屏（grove_lcd_rgb）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_GROVE_LCD_RGB_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_GROVE_LCD_RGB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_GROVE_LCD_RGB_LOG_LEVEL_ERR"></a>

## 364.77 `CONFIG_GROVE_LCD_RGB_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GROVE_LCD_RGB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Seeed Grove LCD RGB 背光（Backlight） → Grove RGB 液晶显示屏（grove_lcd_rgb）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_GROVE_LCD_RGB_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_GROVE_LCD_RGB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_GROVE_LCD_RGB_LOG_LEVEL_INF"></a>

## 364.78 `CONFIG_GROVE_LCD_RGB_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GROVE_LCD_RGB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Seeed Grove LCD RGB 背光（Backlight） → Grove RGB 液晶显示屏（grove_lcd_rgb）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_GROVE_LCD_RGB_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_GROVE_LCD_RGB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_GROVE_LCD_RGB_LOG_LEVEL_OFF"></a>

## 364.79 `CONFIG_GROVE_LCD_RGB_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GROVE_LCD_RGB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Seeed Grove LCD RGB 背光（Backlight） → Grove RGB 液晶显示屏（grove_lcd_rgb）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_GROVE_LCD_RGB_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_GROVE_LCD_RGB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_GROVE_LCD_RGB_LOG_LEVEL_WRN"></a>

## 364.80 `CONFIG_GROVE_LCD_RGB_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_GROVE_LCD_RGB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → Seeed Grove LCD RGB 背光（Backlight） → Grove RGB 液晶显示屏（grove_lcd_rgb）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_GROVE_LCD_RGB_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_GROVE_LCD_RGB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HAPTICS_LOG_LEVEL_CHOICE"></a>

## 364.81 `CONFIG_HAPTICS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：触觉反馈（haptics）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_HAPTICS
```

**默认值（Defaults）**

```text
CONFIG_HAPTICS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_HAPTICS_LOG_LEVEL_OFF
CONFIG_HAPTICS_LOG_LEVEL_ERR
CONFIG_HAPTICS_LOG_LEVEL_WRN
CONFIG_HAPTICS_LOG_LEVEL_INF
CONFIG_HAPTICS_LOG_LEVEL_DBG
CONFIG_HAPTICS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 触觉反馈驱动（Haptic Feedback Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_HAPTICS`](P101_drivers_haptics_配置项参考.md#CONFIG_HAPTICS)、[`CONFIG_HAPTICS_LOG_LEVEL_DEFAULT`](P364_subsys_logging_配置项参考_13.md#CONFIG_HAPTICS_LOG_LEVEL_DEFAULT)、[`CONFIG_HAPTICS_LOG_LEVEL_OFF`](P364_subsys_logging_配置项参考_13.md#CONFIG_HAPTICS_LOG_LEVEL_OFF)、[`CONFIG_HAPTICS_LOG_LEVEL_ERR`](P364_subsys_logging_配置项参考_13.md#CONFIG_HAPTICS_LOG_LEVEL_ERR)、[`CONFIG_HAPTICS_LOG_LEVEL_WRN`](P364_subsys_logging_配置项参考_13.md#CONFIG_HAPTICS_LOG_LEVEL_WRN)、[`CONFIG_HAPTICS_LOG_LEVEL_INF`](P364_subsys_logging_配置项参考_13.md#CONFIG_HAPTICS_LOG_LEVEL_INF)、[`CONFIG_HAPTICS_LOG_LEVEL_DBG`](P364_subsys_logging_配置项参考_13.md#CONFIG_HAPTICS_LOG_LEVEL_DBG)。

<a id="CONFIG_HAPTICS_LOG_LEVEL_DBG"></a>

## 364.82 `CONFIG_HAPTICS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HAPTICS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 触觉反馈驱动（Haptic Feedback Drivers） → 触觉反馈（haptics）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HAPTICS_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_HAPTICS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HAPTICS_LOG_LEVEL_DEFAULT"></a>

## 364.83 `CONFIG_HAPTICS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HAPTICS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 触觉反馈驱动（Haptic Feedback Drivers） → 触觉反馈（haptics）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HAPTICS_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_HAPTICS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HAPTICS_LOG_LEVEL_ERR"></a>

## 364.84 `CONFIG_HAPTICS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HAPTICS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 触觉反馈驱动（Haptic Feedback Drivers） → 触觉反馈（haptics）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HAPTICS_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_HAPTICS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HAPTICS_LOG_LEVEL_INF"></a>

## 364.85 `CONFIG_HAPTICS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HAPTICS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 触觉反馈驱动（Haptic Feedback Drivers） → 触觉反馈（haptics）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HAPTICS_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_HAPTICS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HAPTICS_LOG_LEVEL_OFF"></a>

## 364.86 `CONFIG_HAPTICS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HAPTICS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 触觉反馈驱动（Haptic Feedback Drivers） → 触觉反馈（haptics）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HAPTICS_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_HAPTICS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HAPTICS_LOG_LEVEL_WRN"></a>

## 364.87 `CONFIG_HAPTICS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HAPTICS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 触觉反馈驱动（Haptic Feedback Drivers） → 触觉反馈（haptics）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HAPTICS_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_HAPTICS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HAWKBIT_LOG_LEVEL_CHOICE"></a>

## 364.88 `CONFIG_HAWKBIT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：hawkBit 日志（Log Level for hawkbit）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_HAWKBIT
```

**默认值（Defaults）**

```text
CONFIG_HAWKBIT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_HAWKBIT_LOG_LEVEL_OFF
CONFIG_HAWKBIT_LOG_LEVEL_ERR
CONFIG_HAWKBIT_LOG_LEVEL_WRN
CONFIG_HAWKBIT_LOG_LEVEL_INF
CONFIG_HAWKBIT_LOG_LEVEL_DBG
CONFIG_HAWKBIT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_HAWKBIT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HAWKBIT)、[`CONFIG_HAWKBIT_LOG_LEVEL_DEFAULT`](P364_subsys_logging_配置项参考_13.md#CONFIG_HAWKBIT_LOG_LEVEL_DEFAULT)、[`CONFIG_HAWKBIT_LOG_LEVEL_OFF`](P364_subsys_logging_配置项参考_13.md#CONFIG_HAWKBIT_LOG_LEVEL_OFF)、[`CONFIG_HAWKBIT_LOG_LEVEL_ERR`](P364_subsys_logging_配置项参考_13.md#CONFIG_HAWKBIT_LOG_LEVEL_ERR)、[`CONFIG_HAWKBIT_LOG_LEVEL_WRN`](P364_subsys_logging_配置项参考_13.md#CONFIG_HAWKBIT_LOG_LEVEL_WRN)、[`CONFIG_HAWKBIT_LOG_LEVEL_INF`](P364_subsys_logging_配置项参考_13.md#CONFIG_HAWKBIT_LOG_LEVEL_INF)、[`CONFIG_HAWKBIT_LOG_LEVEL_DBG`](P364_subsys_logging_配置项参考_13.md#CONFIG_HAWKBIT_LOG_LEVEL_DBG)。

<a id="CONFIG_HAWKBIT_LOG_LEVEL_DBG"></a>

## 364.89 `CONFIG_HAWKBIT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HAWKBIT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air） → hawkBit 日志（Log Level for hawkbit）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_HAWKBIT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HAWKBIT_LOG_LEVEL_DEFAULT"></a>

## 364.90 `CONFIG_HAWKBIT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HAWKBIT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air） → hawkBit 日志（Log Level for hawkbit）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_HAWKBIT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HAWKBIT_LOG_LEVEL_ERR"></a>

## 364.91 `CONFIG_HAWKBIT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HAWKBIT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air） → hawkBit 日志（Log Level for hawkbit）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_HAWKBIT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HAWKBIT_LOG_LEVEL_INF"></a>

## 364.92 `CONFIG_HAWKBIT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HAWKBIT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air） → hawkBit 日志（Log Level for hawkbit）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_HAWKBIT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HAWKBIT_LOG_LEVEL_OFF"></a>

## 364.93 `CONFIG_HAWKBIT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HAWKBIT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air） → hawkBit 日志（Log Level for hawkbit）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_HAWKBIT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HAWKBIT_LOG_LEVEL_WRN"></a>

## 364.94 `CONFIG_HAWKBIT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HAWKBIT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → Eclipse hawkBit 固件空中更新支持（Firmware Over-the-Air） → hawkBit 日志（Log Level for hawkbit）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HAWKBIT_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_HAWKBIT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_CHOICE"></a>

## 364.95 `CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：OpenThread 无线电协处理器主机的 HDLC 驱动（HDLC driver for Openthread RCP host）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_HDLC_RCP_IF
```

**默认值（Defaults）**

```text
CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_OFF
CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_ERR
CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_WRN
CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_INF
CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_DBG
CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Zephyr OpenThread 无线电协处理器主机（RCP Host）的高级数据链路控制（HDLC）接口

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_HDLC_RCP_IF`](P102_drivers_hdlc_rcp_if_配置项参考.md#CONFIG_HDLC_RCP_IF)、[`CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_DEFAULT`](P364_subsys_logging_配置项参考_13.md#CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_DEFAULT)、[`CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_OFF`](P364_subsys_logging_配置项参考_13.md#CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_OFF)、[`CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_ERR`](P364_subsys_logging_配置项参考_13.md#CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_ERR)、[`CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_WRN`](P365_subsys_logging_配置项参考_14.md#CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_WRN)、[`CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_INF`](P364_subsys_logging_配置项参考_13.md#CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_INF)、[`CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_DBG`](P364_subsys_logging_配置项参考_13.md#CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_DBG)。

<a id="CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_DBG"></a>

## 364.96 `CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Zephyr OpenThread 无线电协处理器主机（RCP Host）的高级数据链路控制（HDLC）接口 → OpenThread 无线电协处理器主机的 HDLC 驱动（HDLC driver for Openthread RCP host）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_DEFAULT"></a>

## 364.97 `CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Zephyr OpenThread 无线电协处理器主机（RCP Host）的高级数据链路控制（HDLC）接口 → OpenThread 无线电协处理器主机的 HDLC 驱动（HDLC driver for Openthread RCP host）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_ERR"></a>

## 364.98 `CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Zephyr OpenThread 无线电协处理器主机（RCP Host）的高级数据链路控制（HDLC）接口 → OpenThread 无线电协处理器主机的 HDLC 驱动（HDLC driver for Openthread RCP host）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_INF"></a>

## 364.99 `CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Zephyr OpenThread 无线电协处理器主机（RCP Host）的高级数据链路控制（HDLC）接口 → OpenThread 无线电协处理器主机的 HDLC 驱动（HDLC driver for Openthread RCP host）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_OFF"></a>

## 364.100 `CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Zephyr OpenThread 无线电协处理器主机（RCP Host）的高级数据链路控制（HDLC）接口 → OpenThread 无线电协处理器主机的 HDLC 驱动（HDLC driver for Openthread RCP host）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_CHOICE`](P364_subsys_logging_配置项参考_13.md#CONFIG_HDLC_RCP_IF_DRIVER_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P363_subsys_logging_配置项参考_12.md) · [返回大纲](大纲.md) · [下一章](P365_subsys_logging_配置项参考_14.md)
