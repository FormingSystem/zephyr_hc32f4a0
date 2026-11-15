---
id: learning.zephyr-docs.kconfig-reference.page-370
title: "`subsys/logging`配置项参考（19/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第370章\_`subsys/logging`配置项参考（19/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_LV_Z_LOG_LEVEL_DEFAULT"></a>

## 370.1 `CONFIG_LV_Z_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_Z_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → LVGL 图形库（LVGL）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LV_Z_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LV_Z_LOG_LEVEL_ERR"></a>

## 370.2 `CONFIG_LV_Z_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_Z_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → LVGL 图形库（LVGL）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LV_Z_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LV_Z_LOG_LEVEL_INF"></a>

## 370.3 `CONFIG_LV_Z_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_Z_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → LVGL 图形库（LVGL）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LV_Z_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LV_Z_LOG_LEVEL_OFF"></a>

## 370.4 `CONFIG_LV_Z_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_Z_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → LVGL 图形库（LVGL）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LV_Z_LOG_LEVEL_CHOICE)。

<a id="CONFIG_LV_Z_LOG_LEVEL_WRN"></a>

## 370.5 `CONFIG_LV_Z_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_LV_Z_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → LVGL 支持（support） → LVGL 图形库（LVGL）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_LV_Z_LOG_LEVEL_CHOICE`](P369_subsys_logging_配置项参考_18.md#CONFIG_LV_Z_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MBEDTLS_LOG_LEVEL_CHOICE"></a>

## 370.6 `CONFIG_MBEDTLS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：Mbed TLS 库调试钩子的日志（Log level Mbed TLS library debug hook）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MBEDTLS_DEBUG && CONFIG_MBEDTLS
```

**默认值（Defaults）**

```text
CONFIG_MBEDTLS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MBEDTLS_LOG_LEVEL_OFF
CONFIG_MBEDTLS_LOG_LEVEL_ERR
CONFIG_MBEDTLS_LOG_LEVEL_WRN
CONFIG_MBEDTLS_LOG_LEVEL_INF
CONFIG_MBEDTLS_LOG_LEVEL_DBG
CONFIG_MBEDTLS_LOG_LEVEL_DEFAULT
CONFIG_MBEDTLS_LOG_LEVEL_OFF
CONFIG_MBEDTLS_LOG_LEVEL_ERR
CONFIG_MBEDTLS_LOG_LEVEL_WRN
CONFIG_MBEDTLS_LOG_LEVEL_INF
CONFIG_MBEDTLS_LOG_LEVEL_DBG
CONFIG_MBEDTLS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → 启用 Mbed TLS 调试（debug activation）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MBEDTLS_DEBUG`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_DEBUG)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_MBEDTLS_LOG_LEVEL_DEFAULT`](P370_subsys_logging_配置项参考_19.md#CONFIG_MBEDTLS_LOG_LEVEL_DEFAULT)、[`CONFIG_MBEDTLS_LOG_LEVEL_OFF`](P370_subsys_logging_配置项参考_19.md#CONFIG_MBEDTLS_LOG_LEVEL_OFF)、[`CONFIG_MBEDTLS_LOG_LEVEL_ERR`](P370_subsys_logging_配置项参考_19.md#CONFIG_MBEDTLS_LOG_LEVEL_ERR)、[`CONFIG_MBEDTLS_LOG_LEVEL_WRN`](P370_subsys_logging_配置项参考_19.md#CONFIG_MBEDTLS_LOG_LEVEL_WRN)、[`CONFIG_MBEDTLS_LOG_LEVEL_INF`](P370_subsys_logging_配置项参考_19.md#CONFIG_MBEDTLS_LOG_LEVEL_INF)、[`CONFIG_MBEDTLS_LOG_LEVEL_DBG`](P370_subsys_logging_配置项参考_19.md#CONFIG_MBEDTLS_LOG_LEVEL_DBG)。

<a id="CONFIG_MBEDTLS_LOG_LEVEL_DBG"></a>

## 370.7 `CONFIG_MBEDTLS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MBEDTLS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → 启用 Mbed TLS 调试（debug activation） → Mbed TLS 库调试钩子的日志（Log level Mbed TLS library debug hook）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MBEDTLS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MBEDTLS_LOG_LEVEL_DEFAULT"></a>

## 370.8 `CONFIG_MBEDTLS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MBEDTLS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → 启用 Mbed TLS 调试（debug activation） → Mbed TLS 库调试钩子的日志（Log level Mbed TLS library debug hook）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MBEDTLS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MBEDTLS_LOG_LEVEL_ERR"></a>

## 370.9 `CONFIG_MBEDTLS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MBEDTLS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → 启用 Mbed TLS 调试（debug activation） → Mbed TLS 库调试钩子的日志（Log level Mbed TLS library debug hook）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MBEDTLS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MBEDTLS_LOG_LEVEL_INF"></a>

## 370.10 `CONFIG_MBEDTLS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MBEDTLS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → 启用 Mbed TLS 调试（debug activation） → Mbed TLS 库调试钩子的日志（Log level Mbed TLS library debug hook）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MBEDTLS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MBEDTLS_LOG_LEVEL_OFF"></a>

## 370.11 `CONFIG_MBEDTLS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MBEDTLS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → 启用 Mbed TLS 调试（debug activation） → Mbed TLS 库调试钩子的日志（Log level Mbed TLS library debug hook）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MBEDTLS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MBEDTLS_LOG_LEVEL_WRN"></a>

## 370.12 `CONFIG_MBEDTLS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MBEDTLS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → mbedtls（模块路径 `modules/crypto/mbedtls`，相对于 west 工作区顶层目录） → Mbed TLS 支持（Support） → 启用 Mbed TLS 调试（debug activation） → Mbed TLS 库调试钩子的日志（Log level Mbed TLS library debug hook）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MBEDTLS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MBOX_LOG_LEVEL_CHOICE"></a>

## 370.13 `CONFIG_MBOX_LOG_LEVEL_CHOICE`

**提示（Prompt）**：邮箱（mbox）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MBOX
```

**默认值（Defaults）**

```text
CONFIG_MBOX_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MBOX_LOG_LEVEL_OFF
CONFIG_MBOX_LOG_LEVEL_ERR
CONFIG_MBOX_LOG_LEVEL_WRN
CONFIG_MBOX_LOG_LEVEL_INF
CONFIG_MBOX_LOG_LEVEL_DBG
CONFIG_MBOX_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MBOX`](P118_drivers_mbox_配置项参考.md#CONFIG_MBOX)、[`CONFIG_MBOX_LOG_LEVEL_DEFAULT`](P370_subsys_logging_配置项参考_19.md#CONFIG_MBOX_LOG_LEVEL_DEFAULT)、[`CONFIG_MBOX_LOG_LEVEL_OFF`](P370_subsys_logging_配置项参考_19.md#CONFIG_MBOX_LOG_LEVEL_OFF)、[`CONFIG_MBOX_LOG_LEVEL_ERR`](P370_subsys_logging_配置项参考_19.md#CONFIG_MBOX_LOG_LEVEL_ERR)、[`CONFIG_MBOX_LOG_LEVEL_WRN`](P370_subsys_logging_配置项参考_19.md#CONFIG_MBOX_LOG_LEVEL_WRN)、[`CONFIG_MBOX_LOG_LEVEL_INF`](P370_subsys_logging_配置项参考_19.md#CONFIG_MBOX_LOG_LEVEL_INF)、[`CONFIG_MBOX_LOG_LEVEL_DBG`](P370_subsys_logging_配置项参考_19.md#CONFIG_MBOX_LOG_LEVEL_DBG)。

<a id="CONFIG_MBOX_LOG_LEVEL_DBG"></a>

## 370.14 `CONFIG_MBOX_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MBOX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动 → 邮箱（mbox）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MBOX_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MBOX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MBOX_LOG_LEVEL_DEFAULT"></a>

## 370.15 `CONFIG_MBOX_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MBOX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动 → 邮箱（mbox）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MBOX_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MBOX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MBOX_LOG_LEVEL_ERR"></a>

## 370.16 `CONFIG_MBOX_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MBOX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动 → 邮箱（mbox）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MBOX_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MBOX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MBOX_LOG_LEVEL_INF"></a>

## 370.17 `CONFIG_MBOX_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MBOX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动 → 邮箱（mbox）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MBOX_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MBOX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MBOX_LOG_LEVEL_OFF"></a>

## 370.18 `CONFIG_MBOX_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MBOX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动 → 邮箱（mbox）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MBOX_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MBOX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MBOX_LOG_LEVEL_WRN"></a>

## 370.19 `CONFIG_MBOX_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MBOX_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 多通道处理器间邮箱（Multi-Channel Inter-Processor Mailbox，MBOX）驱动 → 邮箱（mbox）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MBOX_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MBOX_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCP_LOG_LEVEL_CHOICE"></a>

## 370.20 `CONFIG_MCP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：MCP 服务器（MCP Server）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MCP_SERVER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_MCP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MCP_LOG_LEVEL_OFF
CONFIG_MCP_LOG_LEVEL_ERR
CONFIG_MCP_LOG_LEVEL_WRN
CONFIG_MCP_LOG_LEVEL_INF
CONFIG_MCP_LOG_LEVEL_DBG
CONFIG_MCP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MCP_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCP_SERVER)、[`CONFIG_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NETWORKING)、[`CONFIG_MCP_LOG_LEVEL_DEFAULT`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCP_LOG_LEVEL_DEFAULT)、[`CONFIG_MCP_LOG_LEVEL_OFF`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCP_LOG_LEVEL_OFF)、[`CONFIG_MCP_LOG_LEVEL_ERR`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCP_LOG_LEVEL_ERR)、[`CONFIG_MCP_LOG_LEVEL_WRN`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCP_LOG_LEVEL_WRN)、[`CONFIG_MCP_LOG_LEVEL_INF`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCP_LOG_LEVEL_INF)、[`CONFIG_MCP_LOG_LEVEL_DBG`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCP_LOG_LEVEL_DBG)。

<a id="CONFIG_MCP_LOG_LEVEL_DBG"></a>

## 370.21 `CONFIG_MCP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】 → MCP 服务器（MCP Server）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCP_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCP_LOG_LEVEL_DEFAULT"></a>

## 370.22 `CONFIG_MCP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】 → MCP 服务器（MCP Server）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCP_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCP_LOG_LEVEL_ERR"></a>

## 370.23 `CONFIG_MCP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】 → MCP 服务器（MCP Server）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCP_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCP_LOG_LEVEL_INF"></a>

## 370.24 `CONFIG_MCP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】 → MCP 服务器（MCP Server）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCP_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCP_LOG_LEVEL_OFF"></a>

## 370.25 `CONFIG_MCP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】 → MCP 服务器（MCP Server）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCP_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCP_LOG_LEVEL_WRN"></a>

## 370.26 `CONFIG_MCP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 模型上下文协议服务器支持（Model Context Protocol，MCP）【实验性 EXPERIMENTAL】 → MCP 服务器（MCP Server）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCP_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCTL_LOG_LEVEL_CHOICE"></a>

## 370.27 `CONFIG_MCTL_LOG_LEVEL_CHOICE`

**提示（Prompt）**：媒体控制（Media control）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MCTL && CONFIG_BT_AUDIO && CONFIG_BT_LOG && CONFIG_BT_HCI && CONFIG_BT
```

**默认值（Defaults）**

```text
CONFIG_MCTL_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MCTL_LOG_LEVEL_INHERIT
CONFIG_MCTL_LOG_LEVEL_OFF
CONFIG_MCTL_LOG_LEVEL_ERR
CONFIG_MCTL_LOG_LEVEL_WRN
CONFIG_MCTL_LOG_LEVEL_INF
CONFIG_MCTL_LOG_LEVEL_DBG
CONFIG_MCTL_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MCTL`](P332_subsys_bluetooth_配置项参考_13.md#CONFIG_MCTL)、[`CONFIG_BT_AUDIO`](P320_subsys_bluetooth_配置项参考_1.md#CONFIG_BT_AUDIO)、[`CONFIG_BT_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_LOG)、[`CONFIG_BT_HCI`](P326_subsys_bluetooth_配置项参考_7.md#CONFIG_BT_HCI)、[`CONFIG_BT`](P013_module_hal_realtek_ameba_配置项参考.md#CONFIG_BT)、[`CONFIG_MCTL_LOG_LEVEL_DEFAULT`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCTL_LOG_LEVEL_DEFAULT)、[`CONFIG_MCTL_LOG_LEVEL_INHERIT`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCTL_LOG_LEVEL_INHERIT)、[`CONFIG_MCTL_LOG_LEVEL_OFF`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCTL_LOG_LEVEL_OFF)、[`CONFIG_MCTL_LOG_LEVEL_ERR`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCTL_LOG_LEVEL_ERR)、[`CONFIG_MCTL_LOG_LEVEL_WRN`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCTL_LOG_LEVEL_WRN)、[`CONFIG_MCTL_LOG_LEVEL_INF`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCTL_LOG_LEVEL_INF)、[`CONFIG_MCTL_LOG_LEVEL_DBG`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCTL_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_BT_LOG`。

<a id="CONFIG_MCTL_LOG_LEVEL_DBG"></a>

## 370.28 `CONFIG_MCTL_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCTL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 媒体控制（Media control）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCTL_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCTL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCTL_LOG_LEVEL_DEFAULT"></a>

## 370.29 `CONFIG_MCTL_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCTL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 媒体控制（Media control）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCTL_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCTL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCTL_LOG_LEVEL_ERR"></a>

## 370.30 `CONFIG_MCTL_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCTL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 媒体控制（Media control）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCTL_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCTL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCTL_LOG_LEVEL_INF"></a>

## 370.31 `CONFIG_MCTL_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCTL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 媒体控制（Media control）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCTL_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCTL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCTL_LOG_LEVEL_INHERIT"></a>

## 370.32 `CONFIG_MCTL_LOG_LEVEL_INHERIT`

**提示（Prompt）**：继承 BT_LOG_LEVEL

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCTL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config_inherit:18`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config_inherit#L18)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 选择项（Choice）：`MCTL_LOG_LEVEL_CHOICE`

**配置项引用（Symbol References）**：[`CONFIG_MCTL_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCTL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCTL_LOG_LEVEL_OFF"></a>

## 370.33 `CONFIG_MCTL_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCTL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 媒体控制（Media control）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCTL_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCTL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCTL_LOG_LEVEL_WRN"></a>

## 370.34 `CONFIG_MCTL_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCTL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 蓝牙（Bluetooth） → 蓝牙日志（Bluetooth logging） → 音频（Audio） → 媒体控制（Media control）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCTL_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCTL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCTP_LOG_LEVEL_CHOICE"></a>

## 370.35 `CONFIG_MCTP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：管理组件传输协议（MCTP）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MCTP
```

**默认值（Defaults）**

```text
CONFIG_MCTP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MCTP_LOG_LEVEL_OFF
CONFIG_MCTP_LOG_LEVEL_ERR
CONFIG_MCTP_LOG_LEVEL_WRN
CONFIG_MCTP_LOG_LEVEL_INF
CONFIG_MCTP_LOG_LEVEL_DBG
CONFIG_MCTP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 平台管理通信基础设施（Platform Management Communications Infrastructure，PMCI） → 管理组件传输协议（Management Component Transport Protocol）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MCTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCTP)、[`CONFIG_MCTP_LOG_LEVEL_DEFAULT`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCTP_LOG_LEVEL_DEFAULT)、[`CONFIG_MCTP_LOG_LEVEL_OFF`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCTP_LOG_LEVEL_OFF)、[`CONFIG_MCTP_LOG_LEVEL_ERR`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCTP_LOG_LEVEL_ERR)、[`CONFIG_MCTP_LOG_LEVEL_WRN`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCTP_LOG_LEVEL_WRN)、[`CONFIG_MCTP_LOG_LEVEL_INF`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCTP_LOG_LEVEL_INF)、[`CONFIG_MCTP_LOG_LEVEL_DBG`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCTP_LOG_LEVEL_DBG)。

<a id="CONFIG_MCTP_LOG_LEVEL_DBG"></a>

## 370.36 `CONFIG_MCTP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 平台管理通信基础设施（Platform Management Communications Infrastructure，PMCI） → 管理组件传输协议（Management Component Transport Protocol）【实验性 EXPERIMENTAL】 → 管理组件传输协议（MCTP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCTP_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCTP_LOG_LEVEL_DEFAULT"></a>

## 370.37 `CONFIG_MCTP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 平台管理通信基础设施（Platform Management Communications Infrastructure，PMCI） → 管理组件传输协议（Management Component Transport Protocol）【实验性 EXPERIMENTAL】 → 管理组件传输协议（MCTP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCTP_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCTP_LOG_LEVEL_ERR"></a>

## 370.38 `CONFIG_MCTP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 平台管理通信基础设施（Platform Management Communications Infrastructure，PMCI） → 管理组件传输协议（Management Component Transport Protocol）【实验性 EXPERIMENTAL】 → 管理组件传输协议（MCTP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCTP_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCTP_LOG_LEVEL_INF"></a>

## 370.39 `CONFIG_MCTP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 平台管理通信基础设施（Platform Management Communications Infrastructure，PMCI） → 管理组件传输协议（Management Component Transport Protocol）【实验性 EXPERIMENTAL】 → 管理组件传输协议（MCTP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCTP_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCTP_LOG_LEVEL_OFF"></a>

## 370.40 `CONFIG_MCTP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 平台管理通信基础设施（Platform Management Communications Infrastructure，PMCI） → 管理组件传输协议（Management Component Transport Protocol）【实验性 EXPERIMENTAL】 → 管理组件传输协议（MCTP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCTP_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCTP_LOG_LEVEL_WRN"></a>

## 370.41 `CONFIG_MCTP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCTP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 平台管理通信基础设施（Platform Management Communications Infrastructure，PMCI） → 管理组件传输协议（Management Component Transport Protocol）【实验性 EXPERIMENTAL】 → 管理组件传输协议（MCTP）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCTP_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCTP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUBOOT_UTIL_LOG_LEVEL_CHOICE"></a>

## 370.42 `CONFIG_MCUBOOT_UTIL_LOG_LEVEL_CHOICE`

**提示（Prompt）**：MCUboot 启动工具（MCUboot bootutil）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MCUBOOT_BOOTUTIL_LIB_OWN_LOG && CONFIG_MCUBOOT_BOOTUTIL_LIB
```

**默认值（Defaults）**

```text
CONFIG_MCUBOOT_UTIL_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MCUBOOT_UTIL_LOG_LEVEL_OFF
CONFIG_MCUBOOT_UTIL_LOG_LEVEL_ERR
CONFIG_MCUBOOT_UTIL_LOG_LEVEL_WRN
CONFIG_MCUBOOT_UTIL_LOG_LEVEL_INF
CONFIG_MCUBOOT_UTIL_LOG_LEVEL_DBG
CONFIG_MCUBOOT_UTIL_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 实用工具库（utility library）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MCUBOOT_BOOTUTIL_LIB_OWN_LOG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUBOOT_BOOTUTIL_LIB_OWN_LOG)、[`CONFIG_MCUBOOT_BOOTUTIL_LIB`](P205_modules_Kconfig.mcuboot_配置项参考.md#CONFIG_MCUBOOT_BOOTUTIL_LIB)、[`CONFIG_MCUBOOT_UTIL_LOG_LEVEL_DEFAULT`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUBOOT_UTIL_LOG_LEVEL_DEFAULT)、[`CONFIG_MCUBOOT_UTIL_LOG_LEVEL_OFF`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUBOOT_UTIL_LOG_LEVEL_OFF)、[`CONFIG_MCUBOOT_UTIL_LOG_LEVEL_ERR`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUBOOT_UTIL_LOG_LEVEL_ERR)、[`CONFIG_MCUBOOT_UTIL_LOG_LEVEL_WRN`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUBOOT_UTIL_LOG_LEVEL_WRN)、[`CONFIG_MCUBOOT_UTIL_LOG_LEVEL_INF`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUBOOT_UTIL_LOG_LEVEL_INF)、[`CONFIG_MCUBOOT_UTIL_LOG_LEVEL_DBG`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUBOOT_UTIL_LOG_LEVEL_DBG)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_MCUBOOT_BOOTUTIL_LIB_OWN_LOG`。

<a id="CONFIG_MCUBOOT_UTIL_LOG_LEVEL_DBG"></a>

## 370.43 `CONFIG_MCUBOOT_UTIL_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUBOOT_UTIL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 实用工具库（utility library） → MCUboot 启动工具（MCUboot bootutil）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_UTIL_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUBOOT_UTIL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUBOOT_UTIL_LOG_LEVEL_DEFAULT"></a>

## 370.44 `CONFIG_MCUBOOT_UTIL_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUBOOT_UTIL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 实用工具库（utility library） → MCUboot 启动工具（MCUboot bootutil）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_UTIL_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUBOOT_UTIL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUBOOT_UTIL_LOG_LEVEL_ERR"></a>

## 370.45 `CONFIG_MCUBOOT_UTIL_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUBOOT_UTIL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 实用工具库（utility library） → MCUboot 启动工具（MCUboot bootutil）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_UTIL_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUBOOT_UTIL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUBOOT_UTIL_LOG_LEVEL_INF"></a>

## 370.46 `CONFIG_MCUBOOT_UTIL_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUBOOT_UTIL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 实用工具库（utility library） → MCUboot 启动工具（MCUboot bootutil）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_UTIL_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUBOOT_UTIL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUBOOT_UTIL_LOG_LEVEL_OFF"></a>

## 370.47 `CONFIG_MCUBOOT_UTIL_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUBOOT_UTIL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 实用工具库（utility library） → MCUboot 启动工具（MCUboot bootutil）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_UTIL_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUBOOT_UTIL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUBOOT_UTIL_LOG_LEVEL_WRN"></a>

## 370.48 `CONFIG_MCUBOOT_UTIL_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUBOOT_UTIL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 模块（Modules） → MCUboot 实用工具库（utility library） → MCUboot 启动工具（MCUboot bootutil）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUBOOT_UTIL_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUBOOT_UTIL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_CHOICE"></a>

## 370.49 `CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_CHOICE`

**提示（Prompt）**：MCUmgr 枚举管理组（mcumgr_grp_enum）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MCUMGR_GRP_ENUM && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_OFF
CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_ERR
CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_WRN
CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_INF
CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_DBG
CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 枚举管理处理程序（enumeration management handlers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MCUMGR_GRP_ENUM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_ENUM)、[`CONFIG_MCUMGR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_DEFAULT`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_DEFAULT)、[`CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_OFF`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_OFF)、[`CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_ERR`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_ERR)、[`CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_WRN`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_WRN)、[`CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_INF`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_INF)、[`CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_DBG`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_DBG)。

<a id="CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_DBG"></a>

## 370.50 `CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 枚举管理处理程序（enumeration management handlers） → MCUmgr 枚举管理组（mcumgr_grp_enum）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_DEFAULT"></a>

## 370.51 `CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 枚举管理处理程序（enumeration management handlers） → MCUmgr 枚举管理组（mcumgr_grp_enum）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_ERR"></a>

## 370.52 `CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 枚举管理处理程序（enumeration management handlers） → MCUmgr 枚举管理组（mcumgr_grp_enum）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_INF"></a>

## 370.53 `CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 枚举管理处理程序（enumeration management handlers） → MCUmgr 枚举管理组（mcumgr_grp_enum）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_OFF"></a>

## 370.54 `CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 枚举管理处理程序（enumeration management handlers） → MCUmgr 枚举管理组（mcumgr_grp_enum）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_WRN"></a>

## 370.55 `CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 枚举管理处理程序（enumeration management handlers） → MCUmgr 枚举管理组（mcumgr_grp_enum）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_ENUM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_CHOICE"></a>

## 370.56 `CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：MCUmgr 文件系统管理组（mcumgr_grp_fs）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MCUMGR_GRP_FS && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_OFF
CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_ERR
CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_WRN
CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_INF
CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_DBG
CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 文件管理处理程序（file management handlers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MCUMGR_GRP_FS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_FS)、[`CONFIG_MCUMGR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_DEFAULT`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_DEFAULT)、[`CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_OFF`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_OFF)、[`CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_ERR`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_ERR)、[`CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_WRN`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_WRN)、[`CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_INF`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_INF)、[`CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_DBG`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_DBG)。

<a id="CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_DBG"></a>

## 370.57 `CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 文件管理处理程序（file management handlers） → MCUmgr 文件系统管理组（mcumgr_grp_fs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_DEFAULT"></a>

## 370.58 `CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 文件管理处理程序（file management handlers） → MCUmgr 文件系统管理组（mcumgr_grp_fs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_ERR"></a>

## 370.59 `CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 文件管理处理程序（file management handlers） → MCUmgr 文件系统管理组（mcumgr_grp_fs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_INF"></a>

## 370.60 `CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 文件管理处理程序（file management handlers） → MCUmgr 文件系统管理组（mcumgr_grp_fs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_OFF"></a>

## 370.61 `CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 文件管理处理程序（file management handlers） → MCUmgr 文件系统管理组（mcumgr_grp_fs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_WRN"></a>

## 370.62 `CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 文件管理处理程序（file management handlers） → MCUmgr 文件系统管理组（mcumgr_grp_fs）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_FS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_CHOICE"></a>

## 370.63 `CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：MCUmgr 映像管理组客户端（mcumgr_grp_img_client）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MCUMGR_GRP_IMG_CLIENT && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_OFF
CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_ERR
CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_WRN
CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_INF
CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_DBG
CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理客户端处理程序（client handlers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MCUMGR_GRP_IMG_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_IMG_CLIENT)、[`CONFIG_MCUMGR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_DEFAULT`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_DEFAULT)、[`CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_OFF`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_OFF)、[`CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_ERR`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_ERR)、[`CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_WRN`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_WRN)、[`CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_INF`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_INF)、[`CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_DBG`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_DBG)。

<a id="CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_DBG"></a>

## 370.64 `CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理客户端处理程序（client handlers） → MCUmgr 映像管理组客户端（mcumgr_grp_img_client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_DEFAULT"></a>

## 370.65 `CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理客户端处理程序（client handlers） → MCUmgr 映像管理组客户端（mcumgr_grp_img_client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_ERR"></a>

## 370.66 `CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理客户端处理程序（client handlers） → MCUmgr 映像管理组客户端（mcumgr_grp_img_client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_INF"></a>

## 370.67 `CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理客户端处理程序（client handlers） → MCUmgr 映像管理组客户端（mcumgr_grp_img_client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_OFF"></a>

## 370.68 `CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理客户端处理程序（client handlers） → MCUmgr 映像管理组客户端（mcumgr_grp_img_client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_WRN"></a>

## 370.69 `CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理客户端处理程序（client handlers） → MCUmgr 映像管理组客户端（mcumgr_grp_img_client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_IMG_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_CHOICE"></a>

## 370.70 `CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_CHOICE`

**提示（Prompt）**：MCUmgr 映像管理组（mcumgr_grp_img）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MCUMGR_GRP_IMG && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_OFF
CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_ERR
CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_WRN
CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_INF
CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_DBG
CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MCUMGR_GRP_IMG`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_IMG)、[`CONFIG_MCUMGR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_DEFAULT`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_DEFAULT)、[`CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_OFF`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_OFF)、[`CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_ERR`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_ERR)、[`CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_WRN`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_WRN)、[`CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_INF`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_INF)、[`CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_DBG`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_DBG)。

<a id="CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_DBG"></a>

## 370.71 `CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers） → MCUmgr 映像管理组（mcumgr_grp_img）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_DEFAULT"></a>

## 370.72 `CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers） → MCUmgr 映像管理组（mcumgr_grp_img）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_ERR"></a>

## 370.73 `CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers） → MCUmgr 映像管理组（mcumgr_grp_img）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_INF"></a>

## 370.74 `CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers） → MCUmgr 映像管理组（mcumgr_grp_img）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_OFF"></a>

## 370.75 `CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers） → MCUmgr 映像管理组（mcumgr_grp_img）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_WRN"></a>

## 370.76 `CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 映像管理处理程序（image management handlers） → MCUmgr 映像管理组（mcumgr_grp_img）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_IMG_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_CHOICE"></a>

## 370.77 `CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：MCUmgr 操作系统管理组客户端（mcumgr_grp_os_client）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MCUMGR_GRP_OS_CLIENT && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_OFF
CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_ERR
CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_WRN
CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_INF
CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_DBG
CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理的客户端请求与响应处理程序（request and response handlers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MCUMGR_GRP_OS_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_OS_CLIENT)、[`CONFIG_MCUMGR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_DEFAULT`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_DEFAULT)、[`CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_OFF`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_OFF)、[`CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_ERR`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_ERR)、[`CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_WRN`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_WRN)、[`CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_INF`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_INF)、[`CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_DBG`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_DBG)。

<a id="CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_DBG"></a>

## 370.78 `CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理的客户端请求与响应处理程序（request and response handlers） → MCUmgr 操作系统管理组客户端（mcumgr_grp_os_client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_DEFAULT"></a>

## 370.79 `CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理的客户端请求与响应处理程序（request and response handlers） → MCUmgr 操作系统管理组客户端（mcumgr_grp_os_client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_ERR"></a>

## 370.80 `CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理的客户端请求与响应处理程序（request and response handlers） → MCUmgr 操作系统管理组客户端（mcumgr_grp_os_client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_INF"></a>

## 370.81 `CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理的客户端请求与响应处理程序（request and response handlers） → MCUmgr 操作系统管理组客户端（mcumgr_grp_os_client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_OFF"></a>

## 370.82 `CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理的客户端请求与响应处理程序（request and response handlers） → MCUmgr 操作系统管理组客户端（mcumgr_grp_os_client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_WRN"></a>

## 370.83 `CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理的客户端请求与响应处理程序（request and response handlers） → MCUmgr 操作系统管理组客户端（mcumgr_grp_os_client）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_OS_CLIENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_CHOICE"></a>

## 370.84 `CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：MCUmgr 操作系统管理组（mcumgr_grp_os）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MCUMGR_GRP_OS && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_OFF
CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_ERR
CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_WRN
CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_INF
CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_DBG
CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MCUMGR_GRP_OS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_OS)、[`CONFIG_MCUMGR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_DEFAULT`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_DEFAULT)、[`CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_OFF`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_OFF)、[`CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_ERR`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_ERR)、[`CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_WRN`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_WRN)、[`CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_INF`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_INF)、[`CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_DBG`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_DBG)。

<a id="CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_DBG"></a>

## 370.85 `CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers） → MCUmgr 操作系统管理组（mcumgr_grp_os）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_DEFAULT"></a>

## 370.86 `CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers） → MCUmgr 操作系统管理组（mcumgr_grp_os）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_ERR"></a>

## 370.87 `CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers） → MCUmgr 操作系统管理组（mcumgr_grp_os）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_INF"></a>

## 370.88 `CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers） → MCUmgr 操作系统管理组（mcumgr_grp_os）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_OFF"></a>

## 370.89 `CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers） → MCUmgr 操作系统管理组（mcumgr_grp_os）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_WRN"></a>

## 370.90 `CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 操作系统管理处理程序（OS management handlers） → MCUmgr 操作系统管理组（mcumgr_grp_os）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_OS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_CHOICE"></a>

## 370.91 `CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_CHOICE`

**提示（Prompt）**：MCUmgr 命令行管理组（mcumgr_grp_shell）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MCUMGR_GRP_SHELL && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_OFF
CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_ERR
CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_WRN
CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_INF
CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_DBG
CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 命令行管理处理程序（shell management handlers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MCUMGR_GRP_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_SHELL)、[`CONFIG_MCUMGR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_DEFAULT`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_DEFAULT)、[`CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_OFF`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_OFF)、[`CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_ERR`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_ERR)、[`CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_WRN`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_WRN)、[`CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_INF`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_INF)、[`CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_DBG`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_DBG)。

<a id="CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_DBG"></a>

## 370.92 `CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 命令行管理处理程序（shell management handlers） → MCUmgr 命令行管理组（mcumgr_grp_shell）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_DEFAULT"></a>

## 370.93 `CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 命令行管理处理程序（shell management handlers） → MCUmgr 命令行管理组（mcumgr_grp_shell）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_ERR"></a>

## 370.94 `CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 命令行管理处理程序（shell management handlers） → MCUmgr 命令行管理组（mcumgr_grp_shell）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_INF"></a>

## 370.95 `CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 命令行管理处理程序（shell management handlers） → MCUmgr 命令行管理组（mcumgr_grp_shell）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_OFF"></a>

## 370.96 `CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 命令行管理处理程序（shell management handlers） → MCUmgr 命令行管理组（mcumgr_grp_shell）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_WRN"></a>

## 370.97 `CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 命令行管理处理程序（shell management handlers） → MCUmgr 命令行管理组（mcumgr_grp_shell）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_SHELL_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_CHOICE"></a>

## 370.98 `CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：MCUmgr 统计管理组（mcumgr_grp_stat）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_MCUMGR_GRP_STAT && CONFIG_MCUMGR
```

**默认值（Defaults）**

```text
CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_OFF
CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_ERR
CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_WRN
CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_INF
CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_DBG
CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 统计管理处理程序（statistics management handlers）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_MCUMGR_GRP_STAT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR_GRP_STAT)、[`CONFIG_MCUMGR`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MCUMGR)、[`CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_DEFAULT`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_DEFAULT)、[`CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_OFF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_OFF)、[`CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_ERR`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_ERR)、[`CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_WRN`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_WRN)、[`CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_INF`](P371_subsys_logging_配置项参考_20.md#CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_INF)、[`CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_DBG`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_DBG)。

<a id="CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_DBG"></a>

## 370.99 `CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 统计管理处理程序（statistics management handlers） → MCUmgr 统计管理组（mcumgr_grp_stat）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_DEFAULT"></a>

## 370.100 `CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 设备管理（Device Management） → 微控制器管理支持（MCUmgr Support） → 命令处理程序（Command Handlers） → MCUmgr 统计管理处理程序（statistics management handlers） → MCUmgr 统计管理组（mcumgr_grp_stat）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_CHOICE`](P370_subsys_logging_配置项参考_19.md#CONFIG_MCUMGR_GRP_STAT_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P369_subsys_logging_配置项参考_18.md) · [返回大纲](大纲.md) · [下一章](P371_subsys_logging_配置项参考_20.md)
