---
id: learning.zephyr-docs.kconfig-reference.page-363
title: "`subsys/logging`配置项参考（12/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第363章\_`subsys/logging`配置项参考（12/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_DISPLAY_LOG_LEVEL_DEFAULT"></a>

## 363.1 `CONFIG_DISPLAY_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISPLAY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 显示（display）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISPLAY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DISPLAY_LOG_LEVEL_ERR"></a>

## 363.2 `CONFIG_DISPLAY_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISPLAY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 显示（display）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISPLAY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DISPLAY_LOG_LEVEL_INF"></a>

## 363.3 `CONFIG_DISPLAY_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISPLAY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 显示（display）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISPLAY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DISPLAY_LOG_LEVEL_OFF"></a>

## 363.4 `CONFIG_DISPLAY_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISPLAY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 显示（display）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISPLAY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DISPLAY_LOG_LEVEL_WRN"></a>

## 363.5 `CONFIG_DISPLAY_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DISPLAY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 显示控制器驱动（Display Controller Drivers） → 显示（display）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DISPLAY_LOG_LEVEL_CHOICE`](P362_subsys_logging_配置项参考_11.md#CONFIG_DISPLAY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DMA_LOG_LEVEL_CHOICE"></a>

## 363.6 `CONFIG_DMA_LOG_LEVEL_CHOICE`

**提示（Prompt）**：直接存储器访问（dma）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_DMA
```

**默认值（Defaults）**

```text
CONFIG_DMA_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_DMA_LOG_LEVEL_OFF
CONFIG_DMA_LOG_LEVEL_ERR
CONFIG_DMA_LOG_LEVEL_WRN
CONFIG_DMA_LOG_LEVEL_INF
CONFIG_DMA_LOG_LEVEL_DBG
CONFIG_DMA_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_DMA`](P079_drivers_dma_配置项参考_1.md#CONFIG_DMA)、[`CONFIG_DMA_LOG_LEVEL_DEFAULT`](P363_subsys_logging_配置项参考_12.md#CONFIG_DMA_LOG_LEVEL_DEFAULT)、[`CONFIG_DMA_LOG_LEVEL_OFF`](P363_subsys_logging_配置项参考_12.md#CONFIG_DMA_LOG_LEVEL_OFF)、[`CONFIG_DMA_LOG_LEVEL_ERR`](P363_subsys_logging_配置项参考_12.md#CONFIG_DMA_LOG_LEVEL_ERR)、[`CONFIG_DMA_LOG_LEVEL_WRN`](P363_subsys_logging_配置项参考_12.md#CONFIG_DMA_LOG_LEVEL_WRN)、[`CONFIG_DMA_LOG_LEVEL_INF`](P363_subsys_logging_配置项参考_12.md#CONFIG_DMA_LOG_LEVEL_INF)、[`CONFIG_DMA_LOG_LEVEL_DBG`](P363_subsys_logging_配置项参考_12.md#CONFIG_DMA_LOG_LEVEL_DBG)。

<a id="CONFIG_DMA_LOG_LEVEL_DBG"></a>

## 363.7 `CONFIG_DMA_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DMA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → 直接存储器访问（dma）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DMA_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_DMA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DMA_LOG_LEVEL_DEFAULT"></a>

## 363.8 `CONFIG_DMA_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DMA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → 直接存储器访问（dma）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DMA_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_DMA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DMA_LOG_LEVEL_ERR"></a>

## 363.9 `CONFIG_DMA_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DMA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → 直接存储器访问（dma）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DMA_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_DMA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DMA_LOG_LEVEL_INF"></a>

## 363.10 `CONFIG_DMA_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DMA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → 直接存储器访问（dma）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DMA_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_DMA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DMA_LOG_LEVEL_OFF"></a>

## 363.11 `CONFIG_DMA_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DMA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → 直接存储器访问（dma）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DMA_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_DMA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DMA_LOG_LEVEL_WRN"></a>

## 363.12 `CONFIG_DMA_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DMA_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 直接内存访问（Direct Memory Access，DMA）驱动 → 直接存储器访问（dma）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DMA_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_DMA_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DP_DRIVER_LOG_LEVEL_CHOICE"></a>

## 363.13 `CONFIG_DP_DRIVER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：DP 驱动（dp drv）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_DP_DRIVER
```

**默认值（Defaults）**

```text
CONFIG_DP_DRIVER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_DP_DRIVER_LOG_LEVEL_OFF
CONFIG_DP_DRIVER_LOG_LEVEL_ERR
CONFIG_DP_DRIVER_LOG_LEVEL_WRN
CONFIG_DP_DRIVER_LOG_LEVEL_INF
CONFIG_DP_DRIVER_LOG_LEVEL_DBG
CONFIG_DP_DRIVER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试端口（Debug Port，DP）驱动【实验性】

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_DP_DRIVER`](P081_drivers_dp_配置项参考.md#CONFIG_DP_DRIVER)、[`CONFIG_DP_DRIVER_LOG_LEVEL_DEFAULT`](P363_subsys_logging_配置项参考_12.md#CONFIG_DP_DRIVER_LOG_LEVEL_DEFAULT)、[`CONFIG_DP_DRIVER_LOG_LEVEL_OFF`](P363_subsys_logging_配置项参考_12.md#CONFIG_DP_DRIVER_LOG_LEVEL_OFF)、[`CONFIG_DP_DRIVER_LOG_LEVEL_ERR`](P363_subsys_logging_配置项参考_12.md#CONFIG_DP_DRIVER_LOG_LEVEL_ERR)、[`CONFIG_DP_DRIVER_LOG_LEVEL_WRN`](P363_subsys_logging_配置项参考_12.md#CONFIG_DP_DRIVER_LOG_LEVEL_WRN)、[`CONFIG_DP_DRIVER_LOG_LEVEL_INF`](P363_subsys_logging_配置项参考_12.md#CONFIG_DP_DRIVER_LOG_LEVEL_INF)、[`CONFIG_DP_DRIVER_LOG_LEVEL_DBG`](P363_subsys_logging_配置项参考_12.md#CONFIG_DP_DRIVER_LOG_LEVEL_DBG)。

<a id="CONFIG_DP_DRIVER_LOG_LEVEL_DBG"></a>

## 363.14 `CONFIG_DP_DRIVER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DP_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试端口（Debug Port，DP）驱动【实验性】 → DP 驱动（dp drv）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DP_DRIVER_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_DP_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DP_DRIVER_LOG_LEVEL_DEFAULT"></a>

## 363.15 `CONFIG_DP_DRIVER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DP_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试端口（Debug Port，DP）驱动【实验性】 → DP 驱动（dp drv）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DP_DRIVER_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_DP_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DP_DRIVER_LOG_LEVEL_ERR"></a>

## 363.16 `CONFIG_DP_DRIVER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DP_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试端口（Debug Port，DP）驱动【实验性】 → DP 驱动（dp drv）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DP_DRIVER_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_DP_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DP_DRIVER_LOG_LEVEL_INF"></a>

## 363.17 `CONFIG_DP_DRIVER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DP_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试端口（Debug Port，DP）驱动【实验性】 → DP 驱动（dp drv）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DP_DRIVER_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_DP_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DP_DRIVER_LOG_LEVEL_OFF"></a>

## 363.18 `CONFIG_DP_DRIVER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DP_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试端口（Debug Port，DP）驱动【实验性】 → DP 驱动（dp drv）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DP_DRIVER_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_DP_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_DP_DRIVER_LOG_LEVEL_WRN"></a>

## 363.19 `CONFIG_DP_DRIVER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_DP_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 调试端口（Debug Port，DP）驱动【实验性】 → DP 驱动（dp drv）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_DP_DRIVER_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_DP_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EC_HC_LOG_LEVEL_CHOICE"></a>

## 363.20 `CONFIG_EC_HC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：嵌入式控制器主机命令（ec-host-commands）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_EC_HOST_CMD
```

**默认值（Defaults）**

```text
CONFIG_EC_HC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_EC_HC_LOG_LEVEL_OFF
CONFIG_EC_HC_LOG_LEVEL_ERR
CONFIG_EC_HC_LOG_LEVEL_WRN
CONFIG_EC_HC_LOG_LEVEL_INF
CONFIG_EC_HC_LOG_LEVEL_DBG
CONFIG_EC_HC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_EC_HOST_CMD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_EC_HOST_CMD)、[`CONFIG_EC_HC_LOG_LEVEL_DEFAULT`](P363_subsys_logging_配置项参考_12.md#CONFIG_EC_HC_LOG_LEVEL_DEFAULT)、[`CONFIG_EC_HC_LOG_LEVEL_OFF`](P363_subsys_logging_配置项参考_12.md#CONFIG_EC_HC_LOG_LEVEL_OFF)、[`CONFIG_EC_HC_LOG_LEVEL_ERR`](P363_subsys_logging_配置项参考_12.md#CONFIG_EC_HC_LOG_LEVEL_ERR)、[`CONFIG_EC_HC_LOG_LEVEL_WRN`](P363_subsys_logging_配置项参考_12.md#CONFIG_EC_HC_LOG_LEVEL_WRN)、[`CONFIG_EC_HC_LOG_LEVEL_INF`](P363_subsys_logging_配置项参考_12.md#CONFIG_EC_HC_LOG_LEVEL_INF)、[`CONFIG_EC_HC_LOG_LEVEL_DBG`](P363_subsys_logging_配置项参考_12.md#CONFIG_EC_HC_LOG_LEVEL_DBG)。

<a id="CONFIG_EC_HC_LOG_LEVEL_DBG"></a>

## 363.21 `CONFIG_EC_HC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EC_HC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。 → 嵌入式控制器主机命令（ec-host-commands）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EC_HC_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EC_HC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EC_HC_LOG_LEVEL_DEFAULT"></a>

## 363.22 `CONFIG_EC_HC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EC_HC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。 → 嵌入式控制器主机命令（ec-host-commands）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EC_HC_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EC_HC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EC_HC_LOG_LEVEL_ERR"></a>

## 363.23 `CONFIG_EC_HC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EC_HC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。 → 嵌入式控制器主机命令（ec-host-commands）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EC_HC_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EC_HC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EC_HC_LOG_LEVEL_INF"></a>

## 363.24 `CONFIG_EC_HC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EC_HC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。 → 嵌入式控制器主机命令（ec-host-commands）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EC_HC_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EC_HC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EC_HC_LOG_LEVEL_OFF"></a>

## 363.25 `CONFIG_EC_HC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EC_HC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。 → 嵌入式控制器主机命令（ec-host-commands）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EC_HC_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EC_HC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EC_HC_LOG_LEVEL_WRN"></a>

## 363.26 `CONFIG_EC_HC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EC_HC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 主机命令处理子系统（Host command handler subsystem） → 支持嵌入式控制器（Embedded Controller）的主机命令处理子系统。 → 嵌入式控制器主机命令（ec-host-commands）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EC_HC_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EC_HC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EDAC_LOG_LEVEL_CHOICE"></a>

## 363.27 `CONFIG_EDAC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：错误检测与纠正（edac）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_EDAC
```

**默认值（Defaults）**

```text
CONFIG_EDAC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_EDAC_LOG_LEVEL_OFF
CONFIG_EDAC_LOG_LEVEL_ERR
CONFIG_EDAC_LOG_LEVEL_WRN
CONFIG_EDAC_LOG_LEVEL_INF
CONFIG_EDAC_LOG_LEVEL_DBG
CONFIG_EDAC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 错误检测与纠正（Error Detection and Correction，EDAC）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_EDAC`](P082_drivers_edac_配置项参考.md#CONFIG_EDAC)、[`CONFIG_EDAC_LOG_LEVEL_DEFAULT`](P363_subsys_logging_配置项参考_12.md#CONFIG_EDAC_LOG_LEVEL_DEFAULT)、[`CONFIG_EDAC_LOG_LEVEL_OFF`](P363_subsys_logging_配置项参考_12.md#CONFIG_EDAC_LOG_LEVEL_OFF)、[`CONFIG_EDAC_LOG_LEVEL_ERR`](P363_subsys_logging_配置项参考_12.md#CONFIG_EDAC_LOG_LEVEL_ERR)、[`CONFIG_EDAC_LOG_LEVEL_WRN`](P363_subsys_logging_配置项参考_12.md#CONFIG_EDAC_LOG_LEVEL_WRN)、[`CONFIG_EDAC_LOG_LEVEL_INF`](P363_subsys_logging_配置项参考_12.md#CONFIG_EDAC_LOG_LEVEL_INF)、[`CONFIG_EDAC_LOG_LEVEL_DBG`](P363_subsys_logging_配置项参考_12.md#CONFIG_EDAC_LOG_LEVEL_DBG)。

<a id="CONFIG_EDAC_LOG_LEVEL_DBG"></a>

## 363.28 `CONFIG_EDAC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EDAC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 错误检测与纠正（Error Detection and Correction，EDAC）驱动 → 错误检测与纠正（edac）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EDAC_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EDAC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EDAC_LOG_LEVEL_DEFAULT"></a>

## 363.29 `CONFIG_EDAC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EDAC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 错误检测与纠正（Error Detection and Correction，EDAC）驱动 → 错误检测与纠正（edac）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EDAC_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EDAC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EDAC_LOG_LEVEL_ERR"></a>

## 363.30 `CONFIG_EDAC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EDAC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 错误检测与纠正（Error Detection and Correction，EDAC）驱动 → 错误检测与纠正（edac）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EDAC_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EDAC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EDAC_LOG_LEVEL_INF"></a>

## 363.31 `CONFIG_EDAC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EDAC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 错误检测与纠正（Error Detection and Correction，EDAC）驱动 → 错误检测与纠正（edac）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EDAC_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EDAC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EDAC_LOG_LEVEL_OFF"></a>

## 363.32 `CONFIG_EDAC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EDAC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 错误检测与纠正（Error Detection and Correction，EDAC）驱动 → 错误检测与纠正（edac）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EDAC_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EDAC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EDAC_LOG_LEVEL_WRN"></a>

## 363.33 `CONFIG_EDAC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EDAC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 错误检测与纠正（Error Detection and Correction，EDAC）驱动 → 错误检测与纠正（edac）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EDAC_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EDAC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EEPROM_LOG_LEVEL_CHOICE"></a>

## 363.34 `CONFIG_EEPROM_LOG_LEVEL_CHOICE`

**提示（Prompt）**：电可擦可编程只读存储器（eeprom）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_EEPROM
```

**默认值（Defaults）**

```text
CONFIG_EEPROM_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_EEPROM_LOG_LEVEL_OFF
CONFIG_EEPROM_LOG_LEVEL_ERR
CONFIG_EEPROM_LOG_LEVEL_WRN
CONFIG_EEPROM_LOG_LEVEL_INF
CONFIG_EEPROM_LOG_LEVEL_DBG
CONFIG_EEPROM_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_EEPROM`](P083_drivers_eeprom_配置项参考.md#CONFIG_EEPROM)、[`CONFIG_EEPROM_LOG_LEVEL_DEFAULT`](P363_subsys_logging_配置项参考_12.md#CONFIG_EEPROM_LOG_LEVEL_DEFAULT)、[`CONFIG_EEPROM_LOG_LEVEL_OFF`](P363_subsys_logging_配置项参考_12.md#CONFIG_EEPROM_LOG_LEVEL_OFF)、[`CONFIG_EEPROM_LOG_LEVEL_ERR`](P363_subsys_logging_配置项参考_12.md#CONFIG_EEPROM_LOG_LEVEL_ERR)、[`CONFIG_EEPROM_LOG_LEVEL_WRN`](P363_subsys_logging_配置项参考_12.md#CONFIG_EEPROM_LOG_LEVEL_WRN)、[`CONFIG_EEPROM_LOG_LEVEL_INF`](P363_subsys_logging_配置项参考_12.md#CONFIG_EEPROM_LOG_LEVEL_INF)、[`CONFIG_EEPROM_LOG_LEVEL_DBG`](P363_subsys_logging_配置项参考_12.md#CONFIG_EEPROM_LOG_LEVEL_DBG)。

<a id="CONFIG_EEPROM_LOG_LEVEL_DBG"></a>

## 363.35 `CONFIG_EEPROM_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EEPROM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动 → 电可擦可编程只读存储器（eeprom）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EEPROM_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EEPROM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EEPROM_LOG_LEVEL_DEFAULT"></a>

## 363.36 `CONFIG_EEPROM_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EEPROM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动 → 电可擦可编程只读存储器（eeprom）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EEPROM_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EEPROM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EEPROM_LOG_LEVEL_ERR"></a>

## 363.37 `CONFIG_EEPROM_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EEPROM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动 → 电可擦可编程只读存储器（eeprom）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EEPROM_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EEPROM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EEPROM_LOG_LEVEL_INF"></a>

## 363.38 `CONFIG_EEPROM_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EEPROM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动 → 电可擦可编程只读存储器（eeprom）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EEPROM_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EEPROM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EEPROM_LOG_LEVEL_OFF"></a>

## 363.39 `CONFIG_EEPROM_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EEPROM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动 → 电可擦可编程只读存储器（eeprom）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EEPROM_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EEPROM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EEPROM_LOG_LEVEL_WRN"></a>

## 363.40 `CONFIG_EEPROM_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EEPROM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 电可擦除可编程只读存储器（Electrically Erasable Programmable Read-Only Memory，EEPROM）驱动 → 电可擦可编程只读存储器（eeprom）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EEPROM_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EEPROM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EMUL_LOG_LEVEL_CHOICE"></a>

## 363.41 `CONFIG_EMUL_LOG_LEVEL_CHOICE`

**提示（Prompt）**：仿真（emul）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_EMUL
```

**默认值（Defaults）**

```text
CONFIG_EMUL_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_EMUL_LOG_LEVEL_OFF
CONFIG_EMUL_LOG_LEVEL_ERR
CONFIG_EMUL_LOG_LEVEL_WRN
CONFIG_EMUL_LOG_LEVEL_INF
CONFIG_EMUL_LOG_LEVEL_DBG
CONFIG_EMUL_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 仿真驱动（Emulation drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_EMUL`](P342_subsys_emul_配置项参考.md#CONFIG_EMUL)、[`CONFIG_EMUL_LOG_LEVEL_DEFAULT`](P363_subsys_logging_配置项参考_12.md#CONFIG_EMUL_LOG_LEVEL_DEFAULT)、[`CONFIG_EMUL_LOG_LEVEL_OFF`](P363_subsys_logging_配置项参考_12.md#CONFIG_EMUL_LOG_LEVEL_OFF)、[`CONFIG_EMUL_LOG_LEVEL_ERR`](P363_subsys_logging_配置项参考_12.md#CONFIG_EMUL_LOG_LEVEL_ERR)、[`CONFIG_EMUL_LOG_LEVEL_WRN`](P363_subsys_logging_配置项参考_12.md#CONFIG_EMUL_LOG_LEVEL_WRN)、[`CONFIG_EMUL_LOG_LEVEL_INF`](P363_subsys_logging_配置项参考_12.md#CONFIG_EMUL_LOG_LEVEL_INF)、[`CONFIG_EMUL_LOG_LEVEL_DBG`](P363_subsys_logging_配置项参考_12.md#CONFIG_EMUL_LOG_LEVEL_DBG)。

<a id="CONFIG_EMUL_LOG_LEVEL_DBG"></a>

## 363.42 `CONFIG_EMUL_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EMUL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 仿真驱动（Emulation drivers） → 仿真（emul）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EMUL_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EMUL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EMUL_LOG_LEVEL_DEFAULT"></a>

## 363.43 `CONFIG_EMUL_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EMUL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 仿真驱动（Emulation drivers） → 仿真（emul）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EMUL_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EMUL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EMUL_LOG_LEVEL_ERR"></a>

## 363.44 `CONFIG_EMUL_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EMUL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 仿真驱动（Emulation drivers） → 仿真（emul）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EMUL_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EMUL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EMUL_LOG_LEVEL_INF"></a>

## 363.45 `CONFIG_EMUL_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EMUL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 仿真驱动（Emulation drivers） → 仿真（emul）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EMUL_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EMUL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EMUL_LOG_LEVEL_OFF"></a>

## 363.46 `CONFIG_EMUL_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EMUL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 仿真驱动（Emulation drivers） → 仿真（emul）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EMUL_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EMUL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EMUL_LOG_LEVEL_WRN"></a>

## 363.47 `CONFIG_EMUL_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EMUL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 仿真驱动（Emulation drivers） → 仿真（emul）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EMUL_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EMUL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ENTROPY_LOG_LEVEL_CHOICE"></a>

## 363.48 `CONFIG_ENTROPY_LOG_LEVEL_CHOICE`

**提示（Prompt）**：熵源（entropy）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_ENTROPY_GENERATOR
```

**默认值（Defaults）**

```text
CONFIG_ENTROPY_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_ENTROPY_LOG_LEVEL_OFF
CONFIG_ENTROPY_LOG_LEVEL_ERR
CONFIG_ENTROPY_LOG_LEVEL_WRN
CONFIG_ENTROPY_LOG_LEVEL_INF
CONFIG_ENTROPY_LOG_LEVEL_DBG
CONFIG_ENTROPY_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_ENTROPY_GENERATOR`](P084_drivers_entropy_配置项参考.md#CONFIG_ENTROPY_GENERATOR)、[`CONFIG_ENTROPY_LOG_LEVEL_DEFAULT`](P363_subsys_logging_配置项参考_12.md#CONFIG_ENTROPY_LOG_LEVEL_DEFAULT)、[`CONFIG_ENTROPY_LOG_LEVEL_OFF`](P363_subsys_logging_配置项参考_12.md#CONFIG_ENTROPY_LOG_LEVEL_OFF)、[`CONFIG_ENTROPY_LOG_LEVEL_ERR`](P363_subsys_logging_配置项参考_12.md#CONFIG_ENTROPY_LOG_LEVEL_ERR)、[`CONFIG_ENTROPY_LOG_LEVEL_WRN`](P363_subsys_logging_配置项参考_12.md#CONFIG_ENTROPY_LOG_LEVEL_WRN)、[`CONFIG_ENTROPY_LOG_LEVEL_INF`](P363_subsys_logging_配置项参考_12.md#CONFIG_ENTROPY_LOG_LEVEL_INF)、[`CONFIG_ENTROPY_LOG_LEVEL_DBG`](P363_subsys_logging_配置项参考_12.md#CONFIG_ENTROPY_LOG_LEVEL_DBG)。

<a id="CONFIG_ENTROPY_LOG_LEVEL_DBG"></a>

## 363.49 `CONFIG_ENTROPY_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ENTROPY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → 熵源（entropy）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_ENTROPY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ENTROPY_LOG_LEVEL_DEFAULT"></a>

## 363.50 `CONFIG_ENTROPY_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ENTROPY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → 熵源（entropy）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_ENTROPY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ENTROPY_LOG_LEVEL_ERR"></a>

## 363.51 `CONFIG_ENTROPY_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ENTROPY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → 熵源（entropy）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_ENTROPY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ENTROPY_LOG_LEVEL_INF"></a>

## 363.52 `CONFIG_ENTROPY_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ENTROPY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → 熵源（entropy）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_ENTROPY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ENTROPY_LOG_LEVEL_OFF"></a>

## 363.53 `CONFIG_ENTROPY_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ENTROPY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → 熵源（entropy）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_ENTROPY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ENTROPY_LOG_LEVEL_WRN"></a>

## 363.54 `CONFIG_ENTROPY_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ENTROPY_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 熵源驱动（Entropy Drivers） → 熵源（entropy）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ENTROPY_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_ENTROPY_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ESPI_LOG_LEVEL_CHOICE"></a>

## 363.55 `CONFIG_ESPI_LOG_LEVEL_CHOICE`

**提示（Prompt）**：增强型串行外设接口（espi）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_ESPI
```

**默认值（Defaults）**

```text
CONFIG_ESPI_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_ESPI_LOG_LEVEL_OFF
CONFIG_ESPI_LOG_LEVEL_ERR
CONFIG_ESPI_LOG_LEVEL_WRN
CONFIG_ESPI_LOG_LEVEL_INF
CONFIG_ESPI_LOG_LEVEL_DBG
CONFIG_ESPI_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_ESPI`](P085_drivers_espi_配置项参考_1.md#CONFIG_ESPI)、[`CONFIG_ESPI_LOG_LEVEL_DEFAULT`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESPI_LOG_LEVEL_DEFAULT)、[`CONFIG_ESPI_LOG_LEVEL_OFF`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESPI_LOG_LEVEL_OFF)、[`CONFIG_ESPI_LOG_LEVEL_ERR`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESPI_LOG_LEVEL_ERR)、[`CONFIG_ESPI_LOG_LEVEL_WRN`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESPI_LOG_LEVEL_WRN)、[`CONFIG_ESPI_LOG_LEVEL_INF`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESPI_LOG_LEVEL_INF)、[`CONFIG_ESPI_LOG_LEVEL_DBG`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESPI_LOG_LEVEL_DBG)。

<a id="CONFIG_ESPI_LOG_LEVEL_DBG"></a>

## 363.56 `CONFIG_ESPI_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → 增强型串行外设接口（espi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ESPI_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ESPI_LOG_LEVEL_DEFAULT"></a>

## 363.57 `CONFIG_ESPI_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → 增强型串行外设接口（espi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ESPI_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ESPI_LOG_LEVEL_ERR"></a>

## 363.58 `CONFIG_ESPI_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → 增强型串行外设接口（espi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ESPI_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ESPI_LOG_LEVEL_INF"></a>

## 363.59 `CONFIG_ESPI_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → 增强型串行外设接口（espi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ESPI_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ESPI_LOG_LEVEL_OFF"></a>

## 363.60 `CONFIG_ESPI_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → 增强型串行外设接口（espi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ESPI_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ESPI_LOG_LEVEL_WRN"></a>

## 363.61 `CONFIG_ESPI_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESPI_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 增强型串行外设接口（Enhanced Serial Peripheral Interface，eSPI）总线驱动 → 增强型串行外设接口（espi）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ESPI_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESPI_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ESP_HAL_LOG_LEVEL_CHOICE"></a>

## 363.62 `CONFIG_ESP_HAL_LOG_LEVEL_CHOICE`

**提示（Prompt）**：ESP 硬件抽象层（esp_hal）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_SOC_FAMILY_ESPRESSIF_ESP32
```

**默认值（Defaults）**

```text
CONFIG_ESP_HAL_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_ESP_HAL_LOG_LEVEL_OFF
CONFIG_ESP_HAL_LOG_LEVEL_ERR
CONFIG_ESP_HAL_LOG_LEVEL_WRN
CONFIG_ESP_HAL_LOG_LEVEL_INF
CONFIG_ESP_HAL_LOG_LEVEL_DBG
CONFIG_ESP_HAL_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SOC_FAMILY_ESPRESSIF_ESP32)、[`CONFIG_ESP_HAL_LOG_LEVEL_DEFAULT`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESP_HAL_LOG_LEVEL_DEFAULT)、[`CONFIG_ESP_HAL_LOG_LEVEL_OFF`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESP_HAL_LOG_LEVEL_OFF)、[`CONFIG_ESP_HAL_LOG_LEVEL_ERR`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESP_HAL_LOG_LEVEL_ERR)、[`CONFIG_ESP_HAL_LOG_LEVEL_WRN`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESP_HAL_LOG_LEVEL_WRN)、[`CONFIG_ESP_HAL_LOG_LEVEL_INF`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESP_HAL_LOG_LEVEL_INF)、[`CONFIG_ESP_HAL_LOG_LEVEL_DBG`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESP_HAL_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_SOC_FAMILY_ESPRESSIF_ESP32`。

<a id="CONFIG_ESP_HAL_LOG_LEVEL_DBG"></a>

## 363.63 `CONFIG_ESP_HAL_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP_HAL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → ESP 硬件抽象层（esp_hal）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ESP_HAL_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESP_HAL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ESP_HAL_LOG_LEVEL_DEFAULT"></a>

## 363.64 `CONFIG_ESP_HAL_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP_HAL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → ESP 硬件抽象层（esp_hal）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ESP_HAL_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESP_HAL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ESP_HAL_LOG_LEVEL_ERR"></a>

## 363.65 `CONFIG_ESP_HAL_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP_HAL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → ESP 硬件抽象层（esp_hal）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ESP_HAL_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESP_HAL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ESP_HAL_LOG_LEVEL_INF"></a>

## 363.66 `CONFIG_ESP_HAL_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP_HAL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → ESP 硬件抽象层（esp_hal）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ESP_HAL_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESP_HAL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ESP_HAL_LOG_LEVEL_OFF"></a>

## 363.67 `CONFIG_ESP_HAL_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP_HAL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → ESP 硬件抽象层（esp_hal）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ESP_HAL_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESP_HAL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ESP_HAL_LOG_LEVEL_WRN"></a>

## 363.68 `CONFIG_ESP_HAL_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP_HAL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → ESP 硬件抽象层（esp_hal）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ESP_HAL_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESP_HAL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_CHOICE"></a>

## 363.69 `CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_CHOICE`

**提示（Prompt）**：ESP Hosted MCU（esp-hosted-mcu）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_ESP_HOSTED_MCU
```

**默认值（Defaults）**

```text
CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_OFF
CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_ERR
CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_WRN
CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_INF
CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_DBG
CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → esp-hosted-mcu 传输核心（Transport Core）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_ESP_HOSTED_MCU`](P123_drivers_misc_配置项参考.md#CONFIG_ESP_HOSTED_MCU)、[`CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_DEFAULT`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_DEFAULT)、[`CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_OFF`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_OFF)、[`CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_ERR`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_ERR)、[`CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_WRN`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_WRN)、[`CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_INF`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_INF)、[`CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_DBG`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_DBG)。

<a id="CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_DBG"></a>

## 363.70 `CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → esp-hosted-mcu 传输核心（Transport Core） → ESP Hosted MCU（esp-hosted-mcu）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_DEFAULT"></a>

## 363.71 `CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → esp-hosted-mcu 传输核心（Transport Core） → ESP Hosted MCU（esp-hosted-mcu）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_ERR"></a>

## 363.72 `CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → esp-hosted-mcu 传输核心（Transport Core） → ESP Hosted MCU（esp-hosted-mcu）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_INF"></a>

## 363.73 `CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → esp-hosted-mcu 传输核心（Transport Core） → ESP Hosted MCU（esp-hosted-mcu）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_OFF"></a>

## 363.74 `CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → esp-hosted-mcu 传输核心（Transport Core） → ESP Hosted MCU（esp-hosted-mcu）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_WRN"></a>

## 363.75 `CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 杂项驱动（Miscellaneous Drivers） → esp-hosted-mcu 传输核心（Transport Core） → ESP Hosted MCU（esp-hosted-mcu）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_ESP_HOSTED_MCU_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EXT2_LOG_LEVEL_CHOICE"></a>

## 363.76 `CONFIG_EXT2_LOG_LEVEL_CHOICE`

**提示（Prompt）**：Ext2 文件系统（Ext2）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_FILE_SYSTEM_EXT2 && CONFIG_FILE_SYSTEM_LIB_LINK
```

**默认值（Defaults）**

```text
CONFIG_EXT2_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_EXT2_LOG_LEVEL_OFF
CONFIG_EXT2_LOG_LEVEL_ERR
CONFIG_EXT2_LOG_LEVEL_WRN
CONFIG_EXT2_LOG_LEVEL_INF
CONFIG_EXT2_LOG_LEVEL_DBG
CONFIG_EXT2_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → Ext2 文件系统支持

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_FILE_SYSTEM_EXT2`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_EXT2)、[`CONFIG_FILE_SYSTEM_LIB_LINK`](P344_subsys_fs_配置项参考.md#CONFIG_FILE_SYSTEM_LIB_LINK)、[`CONFIG_EXT2_LOG_LEVEL_DEFAULT`](P363_subsys_logging_配置项参考_12.md#CONFIG_EXT2_LOG_LEVEL_DEFAULT)、[`CONFIG_EXT2_LOG_LEVEL_OFF`](P363_subsys_logging_配置项参考_12.md#CONFIG_EXT2_LOG_LEVEL_OFF)、[`CONFIG_EXT2_LOG_LEVEL_ERR`](P363_subsys_logging_配置项参考_12.md#CONFIG_EXT2_LOG_LEVEL_ERR)、[`CONFIG_EXT2_LOG_LEVEL_WRN`](P363_subsys_logging_配置项参考_12.md#CONFIG_EXT2_LOG_LEVEL_WRN)、[`CONFIG_EXT2_LOG_LEVEL_INF`](P363_subsys_logging_配置项参考_12.md#CONFIG_EXT2_LOG_LEVEL_INF)、[`CONFIG_EXT2_LOG_LEVEL_DBG`](P363_subsys_logging_配置项参考_12.md#CONFIG_EXT2_LOG_LEVEL_DBG)。

<a id="CONFIG_EXT2_LOG_LEVEL_DBG"></a>

## 363.77 `CONFIG_EXT2_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EXT2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → Ext2 文件系统支持 → Ext2 文件系统（Ext2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EXT2_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EXT2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EXT2_LOG_LEVEL_DEFAULT"></a>

## 363.78 `CONFIG_EXT2_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EXT2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → Ext2 文件系统支持 → Ext2 文件系统（Ext2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EXT2_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EXT2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EXT2_LOG_LEVEL_ERR"></a>

## 363.79 `CONFIG_EXT2_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EXT2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → Ext2 文件系统支持 → Ext2 文件系统（Ext2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EXT2_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EXT2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EXT2_LOG_LEVEL_INF"></a>

## 363.80 `CONFIG_EXT2_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EXT2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → Ext2 文件系统支持 → Ext2 文件系统（Ext2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EXT2_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EXT2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EXT2_LOG_LEVEL_OFF"></a>

## 363.81 `CONFIG_EXT2_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EXT2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → Ext2 文件系统支持 → Ext2 文件系统（Ext2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EXT2_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EXT2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_EXT2_LOG_LEVEL_WRN"></a>

## 363.82 `CONFIG_EXT2_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_EXT2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 文件系统（File Systems） → Ext2 文件系统支持 → Ext2 文件系统（Ext2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_EXT2_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_EXT2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FIDO2_LOG_LEVEL_CHOICE"></a>

## 363.83 `CONFIG_FIDO2_LOG_LEVEL_CHOICE`

**提示（Prompt）**：FIDO2 身份认证（fido2）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_FIDO2
```

**默认值（Defaults）**

```text
CONFIG_FIDO2_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_FIDO2_LOG_LEVEL_OFF
CONFIG_FIDO2_LOG_LEVEL_ERR
CONFIG_FIDO2_LOG_LEVEL_WRN
CONFIG_FIDO2_LOG_LEVEL_INF
CONFIG_FIDO2_LOG_LEVEL_DBG
CONFIG_FIDO2_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_FIDO2`](P318_subsys_authentication_配置项参考.md#CONFIG_FIDO2)、[`CONFIG_FIDO2_LOG_LEVEL_DEFAULT`](P363_subsys_logging_配置项参考_12.md#CONFIG_FIDO2_LOG_LEVEL_DEFAULT)、[`CONFIG_FIDO2_LOG_LEVEL_OFF`](P363_subsys_logging_配置项参考_12.md#CONFIG_FIDO2_LOG_LEVEL_OFF)、[`CONFIG_FIDO2_LOG_LEVEL_ERR`](P363_subsys_logging_配置项参考_12.md#CONFIG_FIDO2_LOG_LEVEL_ERR)、[`CONFIG_FIDO2_LOG_LEVEL_WRN`](P363_subsys_logging_配置项参考_12.md#CONFIG_FIDO2_LOG_LEVEL_WRN)、[`CONFIG_FIDO2_LOG_LEVEL_INF`](P363_subsys_logging_配置项参考_12.md#CONFIG_FIDO2_LOG_LEVEL_INF)、[`CONFIG_FIDO2_LOG_LEVEL_DBG`](P363_subsys_logging_配置项参考_12.md#CONFIG_FIDO2_LOG_LEVEL_DBG)。

<a id="CONFIG_FIDO2_LOG_LEVEL_DBG"></a>

## 363.84 `CONFIG_FIDO2_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FIDO2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → FIDO2 身份认证（fido2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_FIDO2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FIDO2_LOG_LEVEL_DEFAULT"></a>

## 363.85 `CONFIG_FIDO2_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FIDO2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → FIDO2 身份认证（fido2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_FIDO2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FIDO2_LOG_LEVEL_ERR"></a>

## 363.86 `CONFIG_FIDO2_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FIDO2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → FIDO2 身份认证（fido2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_FIDO2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FIDO2_LOG_LEVEL_INF"></a>

## 363.87 `CONFIG_FIDO2_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FIDO2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → FIDO2 身份认证（fido2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_FIDO2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FIDO2_LOG_LEVEL_OFF"></a>

## 363.88 `CONFIG_FIDO2_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FIDO2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → FIDO2 身份认证（fido2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_FIDO2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FIDO2_LOG_LEVEL_WRN"></a>

## 363.89 `CONFIG_FIDO2_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FIDO2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 身份认证（Authentication） → FIDO2 身份验证器（FIDO2 authenticator） → FIDO2 身份认证（fido2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FIDO2_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_FIDO2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FLASHDISK_LOG_LEVEL_CHOICE"></a>

## 363.90 `CONFIG_FLASHDISK_LOG_LEVEL_CHOICE`

**提示（Prompt）**：闪存磁盘（flashdisk）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_DISK_DRIVER_FLASH && CONFIG_DISK_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_FLASHDISK_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_FLASHDISK_LOG_LEVEL_OFF
CONFIG_FLASHDISK_LOG_LEVEL_ERR
CONFIG_FLASHDISK_LOG_LEVEL_WRN
CONFIG_FLASHDISK_LOG_LEVEL_INF
CONFIG_FLASHDISK_LOG_LEVEL_DBG
CONFIG_FLASHDISK_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → 闪存（Flash）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_DISK_DRIVER_FLASH`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVER_FLASH)、[`CONFIG_DISK_DRIVERS`](P076_drivers_disk_配置项参考.md#CONFIG_DISK_DRIVERS)、[`CONFIG_FLASHDISK_LOG_LEVEL_DEFAULT`](P363_subsys_logging_配置项参考_12.md#CONFIG_FLASHDISK_LOG_LEVEL_DEFAULT)、[`CONFIG_FLASHDISK_LOG_LEVEL_OFF`](P363_subsys_logging_配置项参考_12.md#CONFIG_FLASHDISK_LOG_LEVEL_OFF)、[`CONFIG_FLASHDISK_LOG_LEVEL_ERR`](P363_subsys_logging_配置项参考_12.md#CONFIG_FLASHDISK_LOG_LEVEL_ERR)、[`CONFIG_FLASHDISK_LOG_LEVEL_WRN`](P363_subsys_logging_配置项参考_12.md#CONFIG_FLASHDISK_LOG_LEVEL_WRN)、[`CONFIG_FLASHDISK_LOG_LEVEL_INF`](P363_subsys_logging_配置项参考_12.md#CONFIG_FLASHDISK_LOG_LEVEL_INF)、[`CONFIG_FLASHDISK_LOG_LEVEL_DBG`](P363_subsys_logging_配置项参考_12.md#CONFIG_FLASHDISK_LOG_LEVEL_DBG)。

<a id="CONFIG_FLASHDISK_LOG_LEVEL_DBG"></a>

## 363.91 `CONFIG_FLASHDISK_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FLASHDISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → 闪存（Flash） → 闪存磁盘（flashdisk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FLASHDISK_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_FLASHDISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FLASHDISK_LOG_LEVEL_DEFAULT"></a>

## 363.92 `CONFIG_FLASHDISK_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FLASHDISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → 闪存（Flash） → 闪存磁盘（flashdisk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FLASHDISK_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_FLASHDISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FLASHDISK_LOG_LEVEL_ERR"></a>

## 363.93 `CONFIG_FLASHDISK_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FLASHDISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → 闪存（Flash） → 闪存磁盘（flashdisk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FLASHDISK_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_FLASHDISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FLASHDISK_LOG_LEVEL_INF"></a>

## 363.94 `CONFIG_FLASHDISK_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FLASHDISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → 闪存（Flash） → 闪存磁盘（flashdisk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FLASHDISK_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_FLASHDISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FLASHDISK_LOG_LEVEL_OFF"></a>

## 363.95 `CONFIG_FLASHDISK_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FLASHDISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → 闪存（Flash） → 闪存磁盘（flashdisk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FLASHDISK_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_FLASHDISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FLASHDISK_LOG_LEVEL_WRN"></a>

## 363.96 `CONFIG_FLASHDISK_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FLASHDISK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 磁盘驱动（Disk Drivers） → 闪存（Flash） → 闪存磁盘（flashdisk）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FLASHDISK_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_FLASHDISK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FLASH_LOG_LEVEL_CHOICE"></a>

## 363.97 `CONFIG_FLASH_LOG_LEVEL_CHOICE`

**提示（Prompt）**：闪存（flash）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_FLASH
```

**默认值（Defaults）**

```text
CONFIG_FLASH_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_FLASH_LOG_LEVEL_OFF
CONFIG_FLASH_LOG_LEVEL_ERR
CONFIG_FLASH_LOG_LEVEL_WRN
CONFIG_FLASH_LOG_LEVEL_INF
CONFIG_FLASH_LOG_LEVEL_DBG
CONFIG_FLASH_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_FLASH`](P092_drivers_flash_配置项参考_1.md#CONFIG_FLASH)、[`CONFIG_FLASH_LOG_LEVEL_DEFAULT`](P363_subsys_logging_配置项参考_12.md#CONFIG_FLASH_LOG_LEVEL_DEFAULT)、[`CONFIG_FLASH_LOG_LEVEL_OFF`](P364_subsys_logging_配置项参考_13.md#CONFIG_FLASH_LOG_LEVEL_OFF)、[`CONFIG_FLASH_LOG_LEVEL_ERR`](P363_subsys_logging_配置项参考_12.md#CONFIG_FLASH_LOG_LEVEL_ERR)、[`CONFIG_FLASH_LOG_LEVEL_WRN`](P364_subsys_logging_配置项参考_13.md#CONFIG_FLASH_LOG_LEVEL_WRN)、[`CONFIG_FLASH_LOG_LEVEL_INF`](P364_subsys_logging_配置项参考_13.md#CONFIG_FLASH_LOG_LEVEL_INF)、[`CONFIG_FLASH_LOG_LEVEL_DBG`](P363_subsys_logging_配置项参考_12.md#CONFIG_FLASH_LOG_LEVEL_DBG)。

<a id="CONFIG_FLASH_LOG_LEVEL_DBG"></a>

## 363.98 `CONFIG_FLASH_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FLASH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 闪存（flash）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_FLASH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FLASH_LOG_LEVEL_DEFAULT"></a>

## 363.99 `CONFIG_FLASH_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FLASH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 闪存（flash）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_FLASH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_FLASH_LOG_LEVEL_ERR"></a>

## 363.100 `CONFIG_FLASH_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_FLASH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 闪存驱动（Flash Drivers） → 闪存（flash）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_FLASH_LOG_LEVEL_CHOICE`](P363_subsys_logging_配置项参考_12.md#CONFIG_FLASH_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P362_subsys_logging_配置项参考_11.md) · [返回大纲](大纲.md) · [下一章](P364_subsys_logging_配置项参考_13.md)
