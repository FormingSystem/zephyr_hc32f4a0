---
id: learning.zephyr-docs.kconfig-reference.page-380
title: "`subsys/logging`配置项参考（29/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第380章\_`subsys/logging`配置项参考（29/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_USB_MASS_STORAGE_LOG_LEVEL_WRN"></a>

## 380.1 `CONFIG_USB_MASS_STORAGE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_MASS_STORAGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 大容量存储设备类支持（Mass Storage Device Class） → USB 大容量存储（usb mass storage）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_MASS_STORAGE_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_MASS_STORAGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UVB_LOG_LEVEL_CHOICE"></a>

## 380.2 `CONFIG_UVB_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB 虚拟总线服务（USB virtual bus service）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_UVB
```

**默认值（Defaults）**

```text
CONFIG_UVB_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_UVB_LOG_LEVEL_OFF
CONFIG_UVB_LOG_LEVEL_ERR
CONFIG_UVB_LOG_LEVEL_WRN
CONFIG_UVB_LOG_LEVEL_INF
CONFIG_UVB_LOG_LEVEL_DBG
CONFIG_UVB_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 虚拟总线（Virtual Bus）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_UVB`](P180_drivers_usb_配置项参考_2.md#CONFIG_UVB)、[`CONFIG_UVB_LOG_LEVEL_DEFAULT`](P380_subsys_logging_配置项参考_29.md#CONFIG_UVB_LOG_LEVEL_DEFAULT)、[`CONFIG_UVB_LOG_LEVEL_OFF`](P380_subsys_logging_配置项参考_29.md#CONFIG_UVB_LOG_LEVEL_OFF)、[`CONFIG_UVB_LOG_LEVEL_ERR`](P380_subsys_logging_配置项参考_29.md#CONFIG_UVB_LOG_LEVEL_ERR)、[`CONFIG_UVB_LOG_LEVEL_WRN`](P380_subsys_logging_配置项参考_29.md#CONFIG_UVB_LOG_LEVEL_WRN)、[`CONFIG_UVB_LOG_LEVEL_INF`](P380_subsys_logging_配置项参考_29.md#CONFIG_UVB_LOG_LEVEL_INF)、[`CONFIG_UVB_LOG_LEVEL_DBG`](P380_subsys_logging_配置项参考_29.md#CONFIG_UVB_LOG_LEVEL_DBG)。

<a id="CONFIG_UVB_LOG_LEVEL_DBG"></a>

## 380.3 `CONFIG_UVB_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UVB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 虚拟总线（Virtual Bus） → USB 虚拟总线服务（USB virtual bus service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UVB_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_UVB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UVB_LOG_LEVEL_DEFAULT"></a>

## 380.4 `CONFIG_UVB_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UVB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 虚拟总线（Virtual Bus） → USB 虚拟总线服务（USB virtual bus service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UVB_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_UVB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UVB_LOG_LEVEL_ERR"></a>

## 380.5 `CONFIG_UVB_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UVB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 虚拟总线（Virtual Bus） → USB 虚拟总线服务（USB virtual bus service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UVB_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_UVB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UVB_LOG_LEVEL_INF"></a>

## 380.6 `CONFIG_UVB_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UVB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 虚拟总线（Virtual Bus） → USB 虚拟总线服务（USB virtual bus service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UVB_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_UVB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UVB_LOG_LEVEL_OFF"></a>

## 380.7 `CONFIG_UVB_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UVB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 虚拟总线（Virtual Bus） → USB 虚拟总线服务（USB virtual bus service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UVB_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_UVB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_UVB_LOG_LEVEL_WRN"></a>

## 380.8 `CONFIG_UVB_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_UVB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 虚拟总线（Virtual Bus） → USB 虚拟总线服务（USB virtual bus service）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_UVB_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_UVB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VC8000NANOE_LOG_LEVEL_CHOICE"></a>

## 380.9 `CONFIG_VC8000NANOE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：VC8000NanoE 编码器（vc8000nanoe）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_VIDEO_STM32_VENC && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_VC8000NANOE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_VC8000NANOE_LOG_LEVEL_OFF
CONFIG_VC8000NANOE_LOG_LEVEL_ERR
CONFIG_VC8000NANOE_LOG_LEVEL_WRN
CONFIG_VC8000NANOE_LOG_LEVEL_INF
CONFIG_VC8000NANOE_LOG_LEVEL_DBG
CONFIG_VC8000NANOE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → STM32 视频编码器（Video Encoder，VENC）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_VIDEO_STM32_VENC`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_STM32_VENC)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_VC8000NANOE_LOG_LEVEL_DEFAULT`](P380_subsys_logging_配置项参考_29.md#CONFIG_VC8000NANOE_LOG_LEVEL_DEFAULT)、[`CONFIG_VC8000NANOE_LOG_LEVEL_OFF`](P380_subsys_logging_配置项参考_29.md#CONFIG_VC8000NANOE_LOG_LEVEL_OFF)、[`CONFIG_VC8000NANOE_LOG_LEVEL_ERR`](P380_subsys_logging_配置项参考_29.md#CONFIG_VC8000NANOE_LOG_LEVEL_ERR)、[`CONFIG_VC8000NANOE_LOG_LEVEL_WRN`](P380_subsys_logging_配置项参考_29.md#CONFIG_VC8000NANOE_LOG_LEVEL_WRN)、[`CONFIG_VC8000NANOE_LOG_LEVEL_INF`](P380_subsys_logging_配置项参考_29.md#CONFIG_VC8000NANOE_LOG_LEVEL_INF)、[`CONFIG_VC8000NANOE_LOG_LEVEL_DBG`](P380_subsys_logging_配置项参考_29.md#CONFIG_VC8000NANOE_LOG_LEVEL_DBG)。

<a id="CONFIG_VC8000NANOE_LOG_LEVEL_DBG"></a>

## 380.10 `CONFIG_VC8000NANOE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VC8000NANOE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → STM32 视频编码器（Video Encoder，VENC）驱动 → VC8000NanoE 编码器（vc8000nanoe）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VC8000NANOE_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VC8000NANOE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VC8000NANOE_LOG_LEVEL_DEFAULT"></a>

## 380.11 `CONFIG_VC8000NANOE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VC8000NANOE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → STM32 视频编码器（Video Encoder，VENC）驱动 → VC8000NanoE 编码器（vc8000nanoe）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VC8000NANOE_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VC8000NANOE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VC8000NANOE_LOG_LEVEL_ERR"></a>

## 380.12 `CONFIG_VC8000NANOE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VC8000NANOE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → STM32 视频编码器（Video Encoder，VENC）驱动 → VC8000NanoE 编码器（vc8000nanoe）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VC8000NANOE_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VC8000NANOE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VC8000NANOE_LOG_LEVEL_INF"></a>

## 380.13 `CONFIG_VC8000NANOE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VC8000NANOE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → STM32 视频编码器（Video Encoder，VENC）驱动 → VC8000NanoE 编码器（vc8000nanoe）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VC8000NANOE_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VC8000NANOE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VC8000NANOE_LOG_LEVEL_OFF"></a>

## 380.14 `CONFIG_VC8000NANOE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VC8000NANOE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → STM32 视频编码器（Video Encoder，VENC）驱动 → VC8000NanoE 编码器（vc8000nanoe）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VC8000NANOE_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VC8000NANOE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VC8000NANOE_LOG_LEVEL_WRN"></a>

## 380.15 `CONFIG_VC8000NANOE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VC8000NANOE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → STM32 视频编码器（Video Encoder，VENC）驱动 → VC8000NanoE 编码器（vc8000nanoe）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VC8000NANOE_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VC8000NANOE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VIDEO_DRIVERS_LOG_LEVEL_CHOICE"></a>

## 380.16 `CONFIG_VIDEO_DRIVERS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：视频驱动（video_drivers）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_VIDEO_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_VIDEO_DRIVERS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_VIDEO_DRIVERS_LOG_LEVEL_OFF
CONFIG_VIDEO_DRIVERS_LOG_LEVEL_ERR
CONFIG_VIDEO_DRIVERS_LOG_LEVEL_WRN
CONFIG_VIDEO_DRIVERS_LOG_LEVEL_INF
CONFIG_VIDEO_DRIVERS_LOG_LEVEL_DBG
CONFIG_VIDEO_DRIVERS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_VIDEO_DRIVERS`](P182_drivers_video_配置项参考.md#CONFIG_VIDEO_DRIVERS)、[`CONFIG_VIDEO_DRIVERS_LOG_LEVEL_DEFAULT`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIDEO_DRIVERS_LOG_LEVEL_DEFAULT)、[`CONFIG_VIDEO_DRIVERS_LOG_LEVEL_OFF`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIDEO_DRIVERS_LOG_LEVEL_OFF)、[`CONFIG_VIDEO_DRIVERS_LOG_LEVEL_ERR`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIDEO_DRIVERS_LOG_LEVEL_ERR)、[`CONFIG_VIDEO_DRIVERS_LOG_LEVEL_WRN`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIDEO_DRIVERS_LOG_LEVEL_WRN)、[`CONFIG_VIDEO_DRIVERS_LOG_LEVEL_INF`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIDEO_DRIVERS_LOG_LEVEL_INF)、[`CONFIG_VIDEO_DRIVERS_LOG_LEVEL_DBG`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIDEO_DRIVERS_LOG_LEVEL_DBG)。

<a id="CONFIG_VIDEO_DRIVERS_LOG_LEVEL_DBG"></a>

## 380.17 `CONFIG_VIDEO_DRIVERS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIDEO_DRIVERS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 视频驱动（video_drivers）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIDEO_DRIVERS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VIDEO_DRIVERS_LOG_LEVEL_DEFAULT"></a>

## 380.18 `CONFIG_VIDEO_DRIVERS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIDEO_DRIVERS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 视频驱动（video_drivers）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIDEO_DRIVERS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VIDEO_DRIVERS_LOG_LEVEL_ERR"></a>

## 380.19 `CONFIG_VIDEO_DRIVERS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIDEO_DRIVERS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 视频驱动（video_drivers）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIDEO_DRIVERS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VIDEO_DRIVERS_LOG_LEVEL_INF"></a>

## 380.20 `CONFIG_VIDEO_DRIVERS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIDEO_DRIVERS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 视频驱动（video_drivers）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIDEO_DRIVERS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VIDEO_DRIVERS_LOG_LEVEL_OFF"></a>

## 380.21 `CONFIG_VIDEO_DRIVERS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIDEO_DRIVERS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 视频驱动（video_drivers）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIDEO_DRIVERS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VIDEO_DRIVERS_LOG_LEVEL_WRN"></a>

## 380.22 `CONFIG_VIDEO_DRIVERS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIDEO_DRIVERS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 视频驱动（Video Drivers） → 视频驱动（video_drivers）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_DRIVERS_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIDEO_DRIVERS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VIDEO_LOG_LEVEL_CHOICE"></a>

## 380.23 `CONFIG_VIDEO_LOG_LEVEL_CHOICE`

**提示（Prompt）**：视频（video）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_VIDEO
```

**默认值（Defaults）**

```text
CONFIG_VIDEO_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_VIDEO_LOG_LEVEL_OFF
CONFIG_VIDEO_LOG_LEVEL_ERR
CONFIG_VIDEO_LOG_LEVEL_WRN
CONFIG_VIDEO_LOG_LEVEL_INF
CONFIG_VIDEO_LOG_LEVEL_DBG
CONFIG_VIDEO_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 视频子系统（Video subsystem）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_VIDEO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_VIDEO)、[`CONFIG_VIDEO_LOG_LEVEL_DEFAULT`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIDEO_LOG_LEVEL_DEFAULT)、[`CONFIG_VIDEO_LOG_LEVEL_OFF`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIDEO_LOG_LEVEL_OFF)、[`CONFIG_VIDEO_LOG_LEVEL_ERR`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIDEO_LOG_LEVEL_ERR)、[`CONFIG_VIDEO_LOG_LEVEL_WRN`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIDEO_LOG_LEVEL_WRN)、[`CONFIG_VIDEO_LOG_LEVEL_INF`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIDEO_LOG_LEVEL_INF)、[`CONFIG_VIDEO_LOG_LEVEL_DBG`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIDEO_LOG_LEVEL_DBG)。

<a id="CONFIG_VIDEO_LOG_LEVEL_DBG"></a>

## 380.24 `CONFIG_VIDEO_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIDEO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 视频子系统（Video subsystem） → 视频（video）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIDEO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VIDEO_LOG_LEVEL_DEFAULT"></a>

## 380.25 `CONFIG_VIDEO_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIDEO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 视频子系统（Video subsystem） → 视频（video）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIDEO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VIDEO_LOG_LEVEL_ERR"></a>

## 380.26 `CONFIG_VIDEO_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIDEO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 视频子系统（Video subsystem） → 视频（video）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIDEO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VIDEO_LOG_LEVEL_INF"></a>

## 380.27 `CONFIG_VIDEO_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIDEO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 视频子系统（Video subsystem） → 视频（video）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIDEO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VIDEO_LOG_LEVEL_OFF"></a>

## 380.28 `CONFIG_VIDEO_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIDEO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 视频子系统（Video subsystem） → 视频（video）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIDEO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VIDEO_LOG_LEVEL_WRN"></a>

## 380.29 `CONFIG_VIDEO_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIDEO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 视频子系统（Video subsystem） → 视频（video）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VIDEO_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIDEO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VIRTIOFS_LOG_LEVEL_CHOICE"></a>

## 380.30 `CONFIG_VIRTIOFS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：Virtiofs 文件系统（virtiofs）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
CONFIG_VIRTIOFS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_VIRTIOFS_LOG_LEVEL_OFF
CONFIG_VIRTIOFS_LOG_LEVEL_ERR
CONFIG_VIRTIOFS_LOG_LEVEL_WRN
CONFIG_VIRTIOFS_LOG_LEVEL_INF
CONFIG_VIRTIOFS_LOG_LEVEL_DBG
CONFIG_VIRTIOFS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)、[`CONFIG_VIRTIOFS_LOG_LEVEL_DEFAULT`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIRTIOFS_LOG_LEVEL_DEFAULT)、[`CONFIG_VIRTIOFS_LOG_LEVEL_OFF`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIRTIOFS_LOG_LEVEL_OFF)、[`CONFIG_VIRTIOFS_LOG_LEVEL_ERR`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIRTIOFS_LOG_LEVEL_ERR)、[`CONFIG_VIRTIOFS_LOG_LEVEL_WRN`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIRTIOFS_LOG_LEVEL_WRN)、[`CONFIG_VIRTIOFS_LOG_LEVEL_INF`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIRTIOFS_LOG_LEVEL_INF)、[`CONFIG_VIRTIOFS_LOG_LEVEL_DBG`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIRTIOFS_LOG_LEVEL_DBG)。

<a id="CONFIG_VIRTIOFS_LOG_LEVEL_DBG"></a>

## 380.31 `CONFIG_VIRTIOFS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIRTIOFS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → Virtiofs 文件系统（virtiofs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VIRTIOFS_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIRTIOFS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VIRTIOFS_LOG_LEVEL_DEFAULT"></a>

## 380.32 `CONFIG_VIRTIOFS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIRTIOFS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → Virtiofs 文件系统（virtiofs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VIRTIOFS_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIRTIOFS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VIRTIOFS_LOG_LEVEL_ERR"></a>

## 380.33 `CONFIG_VIRTIOFS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIRTIOFS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → Virtiofs 文件系统（virtiofs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VIRTIOFS_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIRTIOFS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VIRTIOFS_LOG_LEVEL_INF"></a>

## 380.34 `CONFIG_VIRTIOFS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIRTIOFS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → Virtiofs 文件系统（virtiofs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VIRTIOFS_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIRTIOFS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VIRTIOFS_LOG_LEVEL_OFF"></a>

## 380.35 `CONFIG_VIRTIOFS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIRTIOFS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → Virtiofs 文件系统（virtiofs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VIRTIOFS_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIRTIOFS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VIRTIOFS_LOG_LEVEL_WRN"></a>

## 380.36 `CONFIG_VIRTIOFS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIRTIOFS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → Virtiofs 文件系统（virtiofs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VIRTIOFS_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIRTIOFS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VIRTIO_LOG_LEVEL_CHOICE"></a>

## 380.37 `CONFIG_VIRTIO_LOG_LEVEL_CHOICE`

**提示（Prompt）**：VirtIO 虚拟输入输出（VIRTIO）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_VIRTIO
```

**默认值（Defaults）**

```text
CONFIG_VIRTIO_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_VIRTIO_LOG_LEVEL_OFF
CONFIG_VIRTIO_LOG_LEVEL_ERR
CONFIG_VIRTIO_LOG_LEVEL_WRN
CONFIG_VIRTIO_LOG_LEVEL_INF
CONFIG_VIRTIO_LOG_LEVEL_DBG
CONFIG_VIRTIO_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → VIRTIO 支持

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_VIRTIO`](P183_drivers_virtio_配置项参考.md#CONFIG_VIRTIO)、[`CONFIG_VIRTIO_LOG_LEVEL_DEFAULT`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIRTIO_LOG_LEVEL_DEFAULT)、[`CONFIG_VIRTIO_LOG_LEVEL_OFF`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIRTIO_LOG_LEVEL_OFF)、[`CONFIG_VIRTIO_LOG_LEVEL_ERR`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIRTIO_LOG_LEVEL_ERR)、[`CONFIG_VIRTIO_LOG_LEVEL_WRN`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIRTIO_LOG_LEVEL_WRN)、[`CONFIG_VIRTIO_LOG_LEVEL_INF`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIRTIO_LOG_LEVEL_INF)、[`CONFIG_VIRTIO_LOG_LEVEL_DBG`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIRTIO_LOG_LEVEL_DBG)。

<a id="CONFIG_VIRTIO_LOG_LEVEL_DBG"></a>

## 380.38 `CONFIG_VIRTIO_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIRTIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → VIRTIO 支持 → VirtIO 虚拟输入输出（VIRTIO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VIRTIO_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIRTIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VIRTIO_LOG_LEVEL_DEFAULT"></a>

## 380.39 `CONFIG_VIRTIO_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIRTIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → VIRTIO 支持 → VirtIO 虚拟输入输出（VIRTIO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VIRTIO_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIRTIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VIRTIO_LOG_LEVEL_ERR"></a>

## 380.40 `CONFIG_VIRTIO_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIRTIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → VIRTIO 支持 → VirtIO 虚拟输入输出（VIRTIO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VIRTIO_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIRTIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VIRTIO_LOG_LEVEL_INF"></a>

## 380.41 `CONFIG_VIRTIO_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIRTIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → VIRTIO 支持 → VirtIO 虚拟输入输出（VIRTIO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VIRTIO_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIRTIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VIRTIO_LOG_LEVEL_OFF"></a>

## 380.42 `CONFIG_VIRTIO_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIRTIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → VIRTIO 支持 → VirtIO 虚拟输入输出（VIRTIO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VIRTIO_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIRTIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_VIRTIO_LOG_LEVEL_WRN"></a>

## 380.43 `CONFIG_VIRTIO_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_VIRTIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → VIRTIO 支持 → VirtIO 虚拟输入输出（VIRTIO）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_VIRTIO_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_VIRTIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_W1_LOG_LEVEL_CHOICE"></a>

## 380.44 `CONFIG_W1_LOG_LEVEL_CHOICE`

**提示（Prompt）**：单线总线（W1）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_W1
```

**默认值（Defaults）**

```text
CONFIG_W1_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_W1_LOG_LEVEL_OFF
CONFIG_W1_LOG_LEVEL_ERR
CONFIG_W1_LOG_LEVEL_WRN
CONFIG_W1_LOG_LEVEL_INF
CONFIG_W1_LOG_LEVEL_DBG
CONFIG_W1_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单总线（1-Wire）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_W1`](P185_drivers_w1_配置项参考.md#CONFIG_W1)、[`CONFIG_W1_LOG_LEVEL_DEFAULT`](P380_subsys_logging_配置项参考_29.md#CONFIG_W1_LOG_LEVEL_DEFAULT)、[`CONFIG_W1_LOG_LEVEL_OFF`](P380_subsys_logging_配置项参考_29.md#CONFIG_W1_LOG_LEVEL_OFF)、[`CONFIG_W1_LOG_LEVEL_ERR`](P380_subsys_logging_配置项参考_29.md#CONFIG_W1_LOG_LEVEL_ERR)、[`CONFIG_W1_LOG_LEVEL_WRN`](P380_subsys_logging_配置项参考_29.md#CONFIG_W1_LOG_LEVEL_WRN)、[`CONFIG_W1_LOG_LEVEL_INF`](P380_subsys_logging_配置项参考_29.md#CONFIG_W1_LOG_LEVEL_INF)、[`CONFIG_W1_LOG_LEVEL_DBG`](P380_subsys_logging_配置项参考_29.md#CONFIG_W1_LOG_LEVEL_DBG)。

<a id="CONFIG_W1_LOG_LEVEL_DBG"></a>

## 380.45 `CONFIG_W1_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_W1_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单总线（1-Wire）驱动 → 单线总线（W1）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_W1_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_W1_LOG_LEVEL_CHOICE)。

<a id="CONFIG_W1_LOG_LEVEL_DEFAULT"></a>

## 380.46 `CONFIG_W1_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_W1_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单总线（1-Wire）驱动 → 单线总线（W1）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_W1_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_W1_LOG_LEVEL_CHOICE)。

<a id="CONFIG_W1_LOG_LEVEL_ERR"></a>

## 380.47 `CONFIG_W1_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_W1_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单总线（1-Wire）驱动 → 单线总线（W1）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_W1_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_W1_LOG_LEVEL_CHOICE)。

<a id="CONFIG_W1_LOG_LEVEL_INF"></a>

## 380.48 `CONFIG_W1_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_W1_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单总线（1-Wire）驱动 → 单线总线（W1）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_W1_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_W1_LOG_LEVEL_CHOICE)。

<a id="CONFIG_W1_LOG_LEVEL_OFF"></a>

## 380.49 `CONFIG_W1_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_W1_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单总线（1-Wire）驱动 → 单线总线（W1）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_W1_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_W1_LOG_LEVEL_CHOICE)。

<a id="CONFIG_W1_LOG_LEVEL_WRN"></a>

## 380.50 `CONFIG_W1_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_W1_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 单总线（1-Wire）驱动 → 单线总线（W1）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_W1_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_W1_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WDT_LOG_LEVEL_CHOICE"></a>

## 380.51 `CONFIG_WDT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：看门狗（watchdog）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_WATCHDOG
```

**默认值（Defaults）**

```text
CONFIG_WDT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_WDT_LOG_LEVEL_OFF
CONFIG_WDT_LOG_LEVEL_ERR
CONFIG_WDT_LOG_LEVEL_WRN
CONFIG_WDT_LOG_LEVEL_INF
CONFIG_WDT_LOG_LEVEL_DBG
CONFIG_WDT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_WATCHDOG`](P186_drivers_watchdog_配置项参考_1.md#CONFIG_WATCHDOG)、[`CONFIG_WDT_LOG_LEVEL_DEFAULT`](P380_subsys_logging_配置项参考_29.md#CONFIG_WDT_LOG_LEVEL_DEFAULT)、[`CONFIG_WDT_LOG_LEVEL_OFF`](P380_subsys_logging_配置项参考_29.md#CONFIG_WDT_LOG_LEVEL_OFF)、[`CONFIG_WDT_LOG_LEVEL_ERR`](P380_subsys_logging_配置项参考_29.md#CONFIG_WDT_LOG_LEVEL_ERR)、[`CONFIG_WDT_LOG_LEVEL_WRN`](P380_subsys_logging_配置项参考_29.md#CONFIG_WDT_LOG_LEVEL_WRN)、[`CONFIG_WDT_LOG_LEVEL_INF`](P380_subsys_logging_配置项参考_29.md#CONFIG_WDT_LOG_LEVEL_INF)、[`CONFIG_WDT_LOG_LEVEL_DBG`](P380_subsys_logging_配置项参考_29.md#CONFIG_WDT_LOG_LEVEL_DBG)。

<a id="CONFIG_WDT_LOG_LEVEL_DBG"></a>

## 380.52 `CONFIG_WDT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WDT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → 看门狗（watchdog）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WDT_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WDT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WDT_LOG_LEVEL_DEFAULT"></a>

## 380.53 `CONFIG_WDT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WDT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → 看门狗（watchdog）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WDT_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WDT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WDT_LOG_LEVEL_ERR"></a>

## 380.54 `CONFIG_WDT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WDT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → 看门狗（watchdog）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WDT_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WDT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WDT_LOG_LEVEL_INF"></a>

## 380.55 `CONFIG_WDT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WDT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → 看门狗（watchdog）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WDT_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WDT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WDT_LOG_LEVEL_OFF"></a>

## 380.56 `CONFIG_WDT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WDT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → 看门狗（watchdog）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WDT_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WDT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WDT_LOG_LEVEL_WRN"></a>

## 380.57 `CONFIG_WDT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WDT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 看门狗驱动（Watchdog Drivers） → 看门狗（watchdog）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WDT_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WDT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_CHOICE"></a>

## 380.58 `CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：Wi-Fi 凭据（wifi_credentials）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_WIFI_CREDENTIALS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_OFF
CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_ERR
CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_WRN
CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_INF
CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_DBG
CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Wi-Fi 凭据管理（credentials management）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_WIFI_CREDENTIALS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_CREDENTIALS)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_DEFAULT`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_DEFAULT)、[`CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_OFF`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_OFF)、[`CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_ERR`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_ERR)、[`CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_WRN`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_WRN)、[`CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_INF`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_INF)、[`CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_DBG`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_DBG)。

<a id="CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_DBG"></a>

## 380.59 `CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Wi-Fi 凭据管理（credentials management） → Wi-Fi 凭据（wifi_credentials）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_DEFAULT"></a>

## 380.60 `CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Wi-Fi 凭据管理（credentials management） → Wi-Fi 凭据（wifi_credentials）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_ERR"></a>

## 380.61 `CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Wi-Fi 凭据管理（credentials management） → Wi-Fi 凭据（wifi_credentials）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_INF"></a>

## 380.62 `CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Wi-Fi 凭据管理（credentials management） → Wi-Fi 凭据（wifi_credentials）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_OFF"></a>

## 380.63 `CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Wi-Fi 凭据管理（credentials management） → Wi-Fi 凭据（wifi_credentials）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_WRN"></a>

## 380.64 `CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络附加服务（Network additional services） → Wi-Fi 凭据管理（credentials management） → Wi-Fi 凭据（wifi_credentials）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_CREDENTIALS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_HWSIM_LOG_LEVEL_CHOICE"></a>

## 380.65 `CONFIG_WIFI_HWSIM_LOG_LEVEL_CHOICE`

**提示（Prompt）**：Wi-Fi 硬件仿真驱动日志（Log level for WiFi hwsim driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_WIFI_HWSIM && CONFIG_WIFI
```

**默认值（Defaults）**

```text
CONFIG_WIFI_HWSIM_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_WIFI_HWSIM_LOG_LEVEL_OFF
CONFIG_WIFI_HWSIM_LOG_LEVEL_ERR
CONFIG_WIFI_HWSIM_LOG_LEVEL_WRN
CONFIG_WIFI_HWSIM_LOG_LEVEL_INF
CONFIG_WIFI_HWSIM_LOG_LEVEL_DBG
CONFIG_WIFI_HWSIM_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 虚拟 Wi-Fi 仿真器驱动（Virtual Wi-Fi simulator driver，hwsim）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_WIFI_HWSIM`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_HWSIM)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_WIFI_HWSIM_LOG_LEVEL_DEFAULT`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_HWSIM_LOG_LEVEL_DEFAULT)、[`CONFIG_WIFI_HWSIM_LOG_LEVEL_OFF`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_HWSIM_LOG_LEVEL_OFF)、[`CONFIG_WIFI_HWSIM_LOG_LEVEL_ERR`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_HWSIM_LOG_LEVEL_ERR)、[`CONFIG_WIFI_HWSIM_LOG_LEVEL_WRN`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_HWSIM_LOG_LEVEL_WRN)、[`CONFIG_WIFI_HWSIM_LOG_LEVEL_INF`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_HWSIM_LOG_LEVEL_INF)、[`CONFIG_WIFI_HWSIM_LOG_LEVEL_DBG`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_HWSIM_LOG_LEVEL_DBG)。

<a id="CONFIG_WIFI_HWSIM_LOG_LEVEL_DBG"></a>

## 380.66 `CONFIG_WIFI_HWSIM_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_HWSIM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 虚拟 Wi-Fi 仿真器驱动（Virtual Wi-Fi simulator driver，hwsim） → Wi-Fi 硬件仿真驱动日志（Log level for WiFi hwsim driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_HWSIM_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_HWSIM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_HWSIM_LOG_LEVEL_DEFAULT"></a>

## 380.67 `CONFIG_WIFI_HWSIM_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_HWSIM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 虚拟 Wi-Fi 仿真器驱动（Virtual Wi-Fi simulator driver，hwsim） → Wi-Fi 硬件仿真驱动日志（Log level for WiFi hwsim driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_HWSIM_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_HWSIM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_HWSIM_LOG_LEVEL_ERR"></a>

## 380.68 `CONFIG_WIFI_HWSIM_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_HWSIM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 虚拟 Wi-Fi 仿真器驱动（Virtual Wi-Fi simulator driver，hwsim） → Wi-Fi 硬件仿真驱动日志（Log level for WiFi hwsim driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_HWSIM_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_HWSIM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_HWSIM_LOG_LEVEL_INF"></a>

## 380.69 `CONFIG_WIFI_HWSIM_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_HWSIM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 虚拟 Wi-Fi 仿真器驱动（Virtual Wi-Fi simulator driver，hwsim） → Wi-Fi 硬件仿真驱动日志（Log level for WiFi hwsim driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_HWSIM_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_HWSIM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_HWSIM_LOG_LEVEL_OFF"></a>

## 380.70 `CONFIG_WIFI_HWSIM_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_HWSIM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 虚拟 Wi-Fi 仿真器驱动（Virtual Wi-Fi simulator driver，hwsim） → Wi-Fi 硬件仿真驱动日志（Log level for WiFi hwsim driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_HWSIM_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_HWSIM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_HWSIM_LOG_LEVEL_WRN"></a>

## 380.71 `CONFIG_WIFI_HWSIM_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_HWSIM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → 虚拟 Wi-Fi 仿真器驱动（Virtual Wi-Fi simulator driver，hwsim） → Wi-Fi 硬件仿真驱动日志（Log level for WiFi hwsim driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_HWSIM_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_HWSIM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_CHOICE"></a>

## 380.72 `CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：WPA 认证请求方（WPA supplicant）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_WIFI_NM_WPA_SUPPLICANT
```

**默认值（Defaults）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_OFF
CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_ERR
CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_WRN
CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_INF
CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_DBG
CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_DEFAULT
CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_OFF
CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_ERR
CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_WRN
CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_INF
CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_DBG
CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_DEFAULT
CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_OFF
CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_ERR
CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_WRN
CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_INF
CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_DBG
CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_DEFAULT`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_DEFAULT)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_OFF`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_OFF)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_ERR`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_ERR)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_WRN`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_WRN)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_INF`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_INF)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_DBG`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_DBG)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_DBG"></a>

## 380.73 `CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → WPA 认证请求方（WPA supplicant）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_DEFAULT"></a>

## 380.74 `CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → WPA 认证请求方（WPA supplicant）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_ERR"></a>

## 380.75 `CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → WPA 认证请求方（WPA supplicant）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_INF"></a>

## 380.76 `CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → WPA 认证请求方（WPA supplicant）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_OFF"></a>

## 380.77 `CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → WPA 认证请求方（WPA supplicant）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_WRN"></a>

## 380.78 `CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → hostap（模块路径 `modules/lib/hostap`，相对于 west 工作区顶层目录） → 来自 hostap 项目的 WPA 认证客户端（WPA Supplicant）［实验性，EXPERIMENTAL］ → WPA 认证请求方（WPA supplicant）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NM_WPA_SUPPLICANT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_CHOICE"></a>

## 380.79 `CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_CHOICE`

**提示（Prompt）**：Wi-Fi nRF70 总线库日志（Log level for Wi-Fi nRF70 bus library）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_NRF70_BUSLIB
```

**默认值（Defaults）**

```text
CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_OFF
CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_ERR
CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_WRN
CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_INF
CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_DBG
CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_DEFAULT
CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_OFF
CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_ERR
CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_WRN
CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_INF
CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_DBG
CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → nrf_wifi（模块路径 `modules/lib/nrf_wifi`，相对于 west 工作区顶层目录） → NRF70 总线库（NRF70 Bus Library）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_NRF70_BUSLIB`](P245_modules_nrf_wifi_配置项参考.md#CONFIG_NRF70_BUSLIB)、[`CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_DEFAULT`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_DEFAULT)、[`CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_OFF`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_OFF)、[`CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_ERR`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_ERR)、[`CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_WRN`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_WRN)、[`CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_INF`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_INF)、[`CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_DBG`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_DBG)。

<a id="CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_DBG"></a>

## 380.80 `CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → nrf_wifi（模块路径 `modules/lib/nrf_wifi`，相对于 west 工作区顶层目录） → NRF70 总线库（NRF70 Bus Library） → Wi-Fi nRF70 总线库日志（Log level for Wi-Fi nRF70 bus library）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_DEFAULT"></a>

## 380.81 `CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → nrf_wifi（模块路径 `modules/lib/nrf_wifi`，相对于 west 工作区顶层目录） → NRF70 总线库（NRF70 Bus Library） → Wi-Fi nRF70 总线库日志（Log level for Wi-Fi nRF70 bus library）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_ERR"></a>

## 380.82 `CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → nrf_wifi（模块路径 `modules/lib/nrf_wifi`，相对于 west 工作区顶层目录） → NRF70 总线库（NRF70 Bus Library） → Wi-Fi nRF70 总线库日志（Log level for Wi-Fi nRF70 bus library）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_INF"></a>

## 380.83 `CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → nrf_wifi（模块路径 `modules/lib/nrf_wifi`，相对于 west 工作区顶层目录） → NRF70 总线库（NRF70 Bus Library） → Wi-Fi nRF70 总线库日志（Log level for Wi-Fi nRF70 bus library）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_OFF"></a>

## 380.84 `CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → nrf_wifi（模块路径 `modules/lib/nrf_wifi`，相对于 west 工作区顶层目录） → NRF70 总线库（NRF70 Bus Library） → Wi-Fi nRF70 总线库日志（Log level for Wi-Fi nRF70 bus library）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_WRN"></a>

## 380.85 `CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → nrf_wifi（模块路径 `modules/lib/nrf_wifi`，相对于 west 工作区顶层目录） → NRF70 总线库（NRF70 Bus Library） → Wi-Fi nRF70 总线库日志（Log level for Wi-Fi nRF70 bus library）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NRF70_BUSLIB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_NRF70_LOG_LEVEL_CHOICE"></a>

## 380.86 `CONFIG_WIFI_NRF70_LOG_LEVEL_CHOICE`

**提示（Prompt）**：Wi-Fi nRF70 驱动日志（Log level for Wi-Fi nRF70 driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_WIFI_NRF70 && CONFIG_WIFI
```

**默认值（Defaults）**

```text
CONFIG_WIFI_NRF70_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_WIFI_NRF70_LOG_LEVEL_OFF
CONFIG_WIFI_NRF70_LOG_LEVEL_ERR
CONFIG_WIFI_NRF70_LOG_LEVEL_WRN
CONFIG_WIFI_NRF70_LOG_LEVEL_INF
CONFIG_WIFI_NRF70_LOG_LEVEL_DBG
CONFIG_WIFI_NRF70_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_WIFI_NRF70`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_NRF70)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_WIFI_NRF70_LOG_LEVEL_DEFAULT`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NRF70_LOG_LEVEL_DEFAULT)、[`CONFIG_WIFI_NRF70_LOG_LEVEL_OFF`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NRF70_LOG_LEVEL_OFF)、[`CONFIG_WIFI_NRF70_LOG_LEVEL_ERR`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NRF70_LOG_LEVEL_ERR)、[`CONFIG_WIFI_NRF70_LOG_LEVEL_WRN`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NRF70_LOG_LEVEL_WRN)、[`CONFIG_WIFI_NRF70_LOG_LEVEL_INF`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NRF70_LOG_LEVEL_INF)、[`CONFIG_WIFI_NRF70_LOG_LEVEL_DBG`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NRF70_LOG_LEVEL_DBG)。

<a id="CONFIG_WIFI_NRF70_LOG_LEVEL_DBG"></a>

## 380.87 `CONFIG_WIFI_NRF70_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NRF70_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → Wi-Fi nRF70 驱动日志（Log level for Wi-Fi nRF70 driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NRF70_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_NRF70_LOG_LEVEL_DEFAULT"></a>

## 380.88 `CONFIG_WIFI_NRF70_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NRF70_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → Wi-Fi nRF70 驱动日志（Log level for Wi-Fi nRF70 driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NRF70_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_NRF70_LOG_LEVEL_ERR"></a>

## 380.89 `CONFIG_WIFI_NRF70_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NRF70_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → Wi-Fi nRF70 驱动日志（Log level for Wi-Fi nRF70 driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NRF70_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_NRF70_LOG_LEVEL_INF"></a>

## 380.90 `CONFIG_WIFI_NRF70_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NRF70_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → Wi-Fi nRF70 驱动日志（Log level for Wi-Fi nRF70 driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NRF70_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_NRF70_LOG_LEVEL_OFF"></a>

## 380.91 `CONFIG_WIFI_NRF70_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NRF70_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → Wi-Fi nRF70 驱动日志（Log level for Wi-Fi nRF70 driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NRF70_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WIFI_NRF70_LOG_LEVEL_WRN"></a>

## 380.92 `CONFIG_WIFI_NRF70_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WIFI_NRF70_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → Wi-Fi 驱动 → nRF70 驱动 → Wi-Fi nRF70 驱动日志（Log level for Wi-Fi nRF70 driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WIFI_NRF70_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WIFI_NRF70_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WUC_LOG_LEVEL_CHOICE"></a>

## 380.93 `CONFIG_WUC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：唤醒控制器（WUC）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_WUC
```

**默认值（Defaults）**

```text
CONFIG_WUC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_WUC_LOG_LEVEL_OFF
CONFIG_WUC_LOG_LEVEL_ERR
CONFIG_WUC_LOG_LEVEL_WRN
CONFIG_WUC_LOG_LEVEL_INF
CONFIG_WUC_LOG_LEVEL_DBG
CONFIG_WUC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 唤醒控制器驱动（Wakeup Controller drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_WUC`](P195_drivers_wuc_配置项参考.md#CONFIG_WUC)、[`CONFIG_WUC_LOG_LEVEL_DEFAULT`](P380_subsys_logging_配置项参考_29.md#CONFIG_WUC_LOG_LEVEL_DEFAULT)、[`CONFIG_WUC_LOG_LEVEL_OFF`](P380_subsys_logging_配置项参考_29.md#CONFIG_WUC_LOG_LEVEL_OFF)、[`CONFIG_WUC_LOG_LEVEL_ERR`](P380_subsys_logging_配置项参考_29.md#CONFIG_WUC_LOG_LEVEL_ERR)、[`CONFIG_WUC_LOG_LEVEL_WRN`](P380_subsys_logging_配置项参考_29.md#CONFIG_WUC_LOG_LEVEL_WRN)、[`CONFIG_WUC_LOG_LEVEL_INF`](P380_subsys_logging_配置项参考_29.md#CONFIG_WUC_LOG_LEVEL_INF)、[`CONFIG_WUC_LOG_LEVEL_DBG`](P380_subsys_logging_配置项参考_29.md#CONFIG_WUC_LOG_LEVEL_DBG)。

<a id="CONFIG_WUC_LOG_LEVEL_DBG"></a>

## 380.94 `CONFIG_WUC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WUC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 唤醒控制器驱动（Wakeup Controller drivers） → 唤醒控制器（WUC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WUC_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WUC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WUC_LOG_LEVEL_DEFAULT"></a>

## 380.95 `CONFIG_WUC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WUC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 唤醒控制器驱动（Wakeup Controller drivers） → 唤醒控制器（WUC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WUC_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WUC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WUC_LOG_LEVEL_ERR"></a>

## 380.96 `CONFIG_WUC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WUC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 唤醒控制器驱动（Wakeup Controller drivers） → 唤醒控制器（WUC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WUC_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WUC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WUC_LOG_LEVEL_INF"></a>

## 380.97 `CONFIG_WUC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WUC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 唤醒控制器驱动（Wakeup Controller drivers） → 唤醒控制器（WUC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WUC_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WUC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WUC_LOG_LEVEL_OFF"></a>

## 380.98 `CONFIG_WUC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WUC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 唤醒控制器驱动（Wakeup Controller drivers） → 唤醒控制器（WUC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WUC_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WUC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_WUC_LOG_LEVEL_WRN"></a>

## 380.99 `CONFIG_WUC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_WUC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 唤醒控制器驱动（Wakeup Controller drivers） → 唤醒控制器（WUC）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_WUC_LOG_LEVEL_CHOICE`](P380_subsys_logging_配置项参考_29.md#CONFIG_WUC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_CHOICE"></a>

## 380.100 `CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：XSI 单进程接口（XSI Single Process）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_POSIX_SYSTEM_INTERFACES
```

**默认值（Defaults）**

```text
CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_OFF
CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_ERR
CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_WRN
CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_INF
CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_DBG
CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 可移植性（Portability） → POSIX API 支持（Support） → POSIX 系统接口（System Interfaces）。 → X/Open 系统接口（system interfaces）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_POSIX_SYSTEM_INTERFACES`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_SYSTEM_INTERFACES)、[`CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_DEFAULT`](P381_subsys_logging_配置项参考_30.md#CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_DEFAULT)、[`CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_OFF`](P381_subsys_logging_配置项参考_30.md#CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_OFF)、[`CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_ERR`](P381_subsys_logging_配置项参考_30.md#CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_ERR)、[`CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_WRN`](P381_subsys_logging_配置项参考_30.md#CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_WRN)、[`CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_INF`](P381_subsys_logging_配置项参考_30.md#CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_INF)、[`CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_DBG`](P381_subsys_logging_配置项参考_30.md#CONFIG_XSI_SINGLE_PROCESS_LOG_LEVEL_DBG)。

<!-- kconfig-navigation -->

[上一章](P379_subsys_logging_配置项参考_28.md) · [返回大纲](大纲.md) · [下一章](P381_subsys_logging_配置项参考_30.md)
