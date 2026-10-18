---
id: learning.zephyr-docs.kconfig-reference.page-379
title: "`subsys/logging`配置项参考（28/30）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第379章\_`subsys/logging`配置项参考（28/30）

本章翻译官方 Kconfig 数据库中 `subsys/logging` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_USBD_MIDI2_LOG_LEVEL_INF"></a>

## 379.1 `CONFIG_USBD_MIDI2_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_MIDI2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB MIDI 2.0 类支持【实验性 EXPERIMENTAL】 → USB 设备 MIDI 2.0 类（usbd midi2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_MIDI2_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_MIDI2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_MIDI2_LOG_LEVEL_OFF"></a>

## 379.2 `CONFIG_USBD_MIDI2_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_MIDI2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB MIDI 2.0 类支持【实验性 EXPERIMENTAL】 → USB 设备 MIDI 2.0 类（usbd midi2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_MIDI2_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_MIDI2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_MIDI2_LOG_LEVEL_WRN"></a>

## 379.3 `CONFIG_USBD_MIDI2_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_MIDI2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB MIDI 2.0 类支持【实验性 EXPERIMENTAL】 → USB 设备 MIDI 2.0 类（usbd midi2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_MIDI2_LOG_LEVEL_CHOICE`](P378_subsys_logging_配置项参考_27.md#CONFIG_USBD_MIDI2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_MSC_LOG_LEVEL_CHOICE"></a>

## 379.4 `CONFIG_USBD_MSC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB 大容量存储设备类（usbd msc）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USBD_MSC_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
CONFIG_USBD_MSC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USBD_MSC_LOG_LEVEL_OFF
CONFIG_USBD_MSC_LOG_LEVEL_ERR
CONFIG_USBD_MSC_LOG_LEVEL_WRN
CONFIG_USBD_MSC_LOG_LEVEL_INF
CONFIG_USBD_MSC_LOG_LEVEL_DBG
CONFIG_USBD_MSC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 大容量存储设备类支持（Mass Storage Device class）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USBD_MSC_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_MSC_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK_NEXT)、[`CONFIG_USBD_MSC_LOG_LEVEL_DEFAULT`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_MSC_LOG_LEVEL_DEFAULT)、[`CONFIG_USBD_MSC_LOG_LEVEL_OFF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_MSC_LOG_LEVEL_OFF)、[`CONFIG_USBD_MSC_LOG_LEVEL_ERR`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_MSC_LOG_LEVEL_ERR)、[`CONFIG_USBD_MSC_LOG_LEVEL_WRN`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_MSC_LOG_LEVEL_WRN)、[`CONFIG_USBD_MSC_LOG_LEVEL_INF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_MSC_LOG_LEVEL_INF)、[`CONFIG_USBD_MSC_LOG_LEVEL_DBG`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_MSC_LOG_LEVEL_DBG)。

<a id="CONFIG_USBD_MSC_LOG_LEVEL_DBG"></a>

## 379.5 `CONFIG_USBD_MSC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_MSC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 大容量存储设备类支持（Mass Storage Device class） → USB 大容量存储设备类（usbd msc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_MSC_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_MSC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_MSC_LOG_LEVEL_DEFAULT"></a>

## 379.6 `CONFIG_USBD_MSC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_MSC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 大容量存储设备类支持（Mass Storage Device class） → USB 大容量存储设备类（usbd msc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_MSC_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_MSC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_MSC_LOG_LEVEL_ERR"></a>

## 379.7 `CONFIG_USBD_MSC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_MSC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 大容量存储设备类支持（Mass Storage Device class） → USB 大容量存储设备类（usbd msc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_MSC_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_MSC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_MSC_LOG_LEVEL_INF"></a>

## 379.8 `CONFIG_USBD_MSC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_MSC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 大容量存储设备类支持（Mass Storage Device class） → USB 大容量存储设备类（usbd msc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_MSC_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_MSC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_MSC_LOG_LEVEL_OFF"></a>

## 379.9 `CONFIG_USBD_MSC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_MSC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 大容量存储设备类支持（Mass Storage Device class） → USB 大容量存储设备类（usbd msc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_MSC_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_MSC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_MSC_LOG_LEVEL_WRN"></a>

## 379.10 `CONFIG_USBD_MSC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_MSC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 大容量存储设备类支持（Mass Storage Device class） → USB 大容量存储设备类（usbd msc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_MSC_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_MSC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_UAC2_LOG_LEVEL_CHOICE"></a>

## 379.11 `CONFIG_USBD_UAC2_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB 设备音频类 2.0（usbd uac2）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USBD_AUDIO2_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
CONFIG_USBD_UAC2_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USBD_UAC2_LOG_LEVEL_OFF
CONFIG_USBD_UAC2_LOG_LEVEL_ERR
CONFIG_USBD_UAC2_LOG_LEVEL_WRN
CONFIG_USBD_UAC2_LOG_LEVEL_INF
CONFIG_USBD_UAC2_LOG_LEVEL_DBG
CONFIG_USBD_UAC2_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 音频类 2 支持（Audio 2 class）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USBD_AUDIO2_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_AUDIO2_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK_NEXT)、[`CONFIG_USBD_UAC2_LOG_LEVEL_DEFAULT`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_UAC2_LOG_LEVEL_DEFAULT)、[`CONFIG_USBD_UAC2_LOG_LEVEL_OFF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_UAC2_LOG_LEVEL_OFF)、[`CONFIG_USBD_UAC2_LOG_LEVEL_ERR`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_UAC2_LOG_LEVEL_ERR)、[`CONFIG_USBD_UAC2_LOG_LEVEL_WRN`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_UAC2_LOG_LEVEL_WRN)、[`CONFIG_USBD_UAC2_LOG_LEVEL_INF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_UAC2_LOG_LEVEL_INF)、[`CONFIG_USBD_UAC2_LOG_LEVEL_DBG`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_UAC2_LOG_LEVEL_DBG)。

<a id="CONFIG_USBD_UAC2_LOG_LEVEL_DBG"></a>

## 379.12 `CONFIG_USBD_UAC2_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_UAC2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 音频类 2 支持（Audio 2 class） → USB 设备音频类 2.0（usbd uac2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_UAC2_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_UAC2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_UAC2_LOG_LEVEL_DEFAULT"></a>

## 379.13 `CONFIG_USBD_UAC2_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_UAC2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 音频类 2 支持（Audio 2 class） → USB 设备音频类 2.0（usbd uac2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_UAC2_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_UAC2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_UAC2_LOG_LEVEL_ERR"></a>

## 379.14 `CONFIG_USBD_UAC2_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_UAC2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 音频类 2 支持（Audio 2 class） → USB 设备音频类 2.0（usbd uac2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_UAC2_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_UAC2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_UAC2_LOG_LEVEL_INF"></a>

## 379.15 `CONFIG_USBD_UAC2_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_UAC2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 音频类 2 支持（Audio 2 class） → USB 设备音频类 2.0（usbd uac2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_UAC2_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_UAC2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_UAC2_LOG_LEVEL_OFF"></a>

## 379.16 `CONFIG_USBD_UAC2_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_UAC2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 音频类 2 支持（Audio 2 class） → USB 设备音频类 2.0（usbd uac2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_UAC2_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_UAC2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_UAC2_LOG_LEVEL_WRN"></a>

## 379.17 `CONFIG_USBD_UAC2_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_UAC2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 音频类 2 支持（Audio 2 class） → USB 设备音频类 2.0（usbd uac2）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_UAC2_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_UAC2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_VIDEO_LOG_LEVEL_CHOICE"></a>

## 379.18 `CONFIG_USBD_VIDEO_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB 设备视频类（usbd uvc）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USBD_VIDEO_CLASS && CONFIG_USB_DEVICE_STACK_NEXT
```

**默认值（Defaults）**

```text
CONFIG_USBD_VIDEO_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USBD_VIDEO_LOG_LEVEL_OFF
CONFIG_USBD_VIDEO_LOG_LEVEL_ERR
CONFIG_USBD_VIDEO_LOG_LEVEL_WRN
CONFIG_USBD_VIDEO_LOG_LEVEL_INF
CONFIG_USBD_VIDEO_LOG_LEVEL_DBG
CONFIG_USBD_VIDEO_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 视频类实现（Video Class）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USBD_VIDEO_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBD_VIDEO_CLASS)、[`CONFIG_USB_DEVICE_STACK_NEXT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK_NEXT)、[`CONFIG_USBD_VIDEO_LOG_LEVEL_DEFAULT`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_VIDEO_LOG_LEVEL_DEFAULT)、[`CONFIG_USBD_VIDEO_LOG_LEVEL_OFF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_VIDEO_LOG_LEVEL_OFF)、[`CONFIG_USBD_VIDEO_LOG_LEVEL_ERR`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_VIDEO_LOG_LEVEL_ERR)、[`CONFIG_USBD_VIDEO_LOG_LEVEL_WRN`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_VIDEO_LOG_LEVEL_WRN)、[`CONFIG_USBD_VIDEO_LOG_LEVEL_INF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_VIDEO_LOG_LEVEL_INF)、[`CONFIG_USBD_VIDEO_LOG_LEVEL_DBG`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_VIDEO_LOG_LEVEL_DBG)。

<a id="CONFIG_USBD_VIDEO_LOG_LEVEL_DBG"></a>

## 379.19 `CONFIG_USBD_VIDEO_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_VIDEO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 视频类实现（Video Class）【实验性 EXPERIMENTAL】 → USB 设备视频类（usbd uvc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_VIDEO_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_VIDEO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_VIDEO_LOG_LEVEL_DEFAULT"></a>

## 379.20 `CONFIG_USBD_VIDEO_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_VIDEO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 视频类实现（Video Class）【实验性 EXPERIMENTAL】 → USB 设备视频类（usbd uvc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_VIDEO_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_VIDEO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_VIDEO_LOG_LEVEL_ERR"></a>

## 379.21 `CONFIG_USBD_VIDEO_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_VIDEO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 视频类实现（Video Class）【实验性 EXPERIMENTAL】 → USB 设备视频类（usbd uvc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_VIDEO_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_VIDEO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_VIDEO_LOG_LEVEL_INF"></a>

## 379.22 `CONFIG_USBD_VIDEO_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_VIDEO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 视频类实现（Video Class）【实验性 EXPERIMENTAL】 → USB 设备视频类（usbd uvc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_VIDEO_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_VIDEO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_VIDEO_LOG_LEVEL_OFF"></a>

## 379.23 `CONFIG_USBD_VIDEO_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_VIDEO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 视频类实现（Video Class）【实验性 EXPERIMENTAL】 → USB 设备视频类（usbd uvc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_VIDEO_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_VIDEO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBD_VIDEO_LOG_LEVEL_WRN"></a>

## 379.24 `CONFIG_USBD_VIDEO_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBD_VIDEO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 新 USB 设备协议栈（device stack） → USB 视频类实现（Video Class）【实验性 EXPERIMENTAL】 → USB 设备视频类（usbd uvc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBD_VIDEO_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBD_VIDEO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBH_HUB_LOG_LEVEL_CHOICE"></a>

## 379.25 `CONFIG_USBH_HUB_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB 主机集线器（usbh hub）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USBH_HUB_CLASS && CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
CONFIG_USBH_HUB_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USBH_HUB_LOG_LEVEL_OFF
CONFIG_USBH_HUB_LOG_LEVEL_ERR
CONFIG_USBH_HUB_LOG_LEVEL_WRN
CONFIG_USBH_HUB_LOG_LEVEL_INF
CONFIG_USBH_HUB_LOG_LEVEL_DBG
CONFIG_USBH_HUB_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机集线器类驱动（Host Hub Class Driver）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USBH_HUB_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBH_HUB_CLASS)、[`CONFIG_USB_HOST_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_HOST_STACK)、[`CONFIG_USBH_HUB_LOG_LEVEL_DEFAULT`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_HUB_LOG_LEVEL_DEFAULT)、[`CONFIG_USBH_HUB_LOG_LEVEL_OFF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_HUB_LOG_LEVEL_OFF)、[`CONFIG_USBH_HUB_LOG_LEVEL_ERR`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_HUB_LOG_LEVEL_ERR)、[`CONFIG_USBH_HUB_LOG_LEVEL_WRN`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_HUB_LOG_LEVEL_WRN)、[`CONFIG_USBH_HUB_LOG_LEVEL_INF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_HUB_LOG_LEVEL_INF)、[`CONFIG_USBH_HUB_LOG_LEVEL_DBG`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_HUB_LOG_LEVEL_DBG)。

<a id="CONFIG_USBH_HUB_LOG_LEVEL_DBG"></a>

## 379.26 `CONFIG_USBH_HUB_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBH_HUB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机集线器类驱动（Host Hub Class Driver） → USB 主机集线器（usbh hub）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBH_HUB_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_HUB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBH_HUB_LOG_LEVEL_DEFAULT"></a>

## 379.27 `CONFIG_USBH_HUB_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBH_HUB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机集线器类驱动（Host Hub Class Driver） → USB 主机集线器（usbh hub）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBH_HUB_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_HUB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBH_HUB_LOG_LEVEL_ERR"></a>

## 379.28 `CONFIG_USBH_HUB_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBH_HUB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机集线器类驱动（Host Hub Class Driver） → USB 主机集线器（usbh hub）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBH_HUB_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_HUB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBH_HUB_LOG_LEVEL_INF"></a>

## 379.29 `CONFIG_USBH_HUB_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBH_HUB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机集线器类驱动（Host Hub Class Driver） → USB 主机集线器（usbh hub）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBH_HUB_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_HUB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBH_HUB_LOG_LEVEL_OFF"></a>

## 379.30 `CONFIG_USBH_HUB_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBH_HUB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机集线器类驱动（Host Hub Class Driver） → USB 主机集线器（usbh hub）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBH_HUB_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_HUB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBH_HUB_LOG_LEVEL_WRN"></a>

## 379.31 `CONFIG_USBH_HUB_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBH_HUB_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机集线器类驱动（Host Hub Class Driver） → USB 主机集线器（usbh hub）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBH_HUB_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_HUB_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBH_LOG_LEVEL_CHOICE"></a>

## 379.32 `CONFIG_USBH_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB 主机（usbh）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
CONFIG_USBH_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USBH_LOG_LEVEL_OFF
CONFIG_USBH_LOG_LEVEL_ERR
CONFIG_USBH_LOG_LEVEL_WRN
CONFIG_USBH_LOG_LEVEL_INF
CONFIG_USBH_LOG_LEVEL_DBG
CONFIG_USBH_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USB_HOST_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_HOST_STACK)、[`CONFIG_USBH_LOG_LEVEL_DEFAULT`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_LOG_LEVEL_DEFAULT)、[`CONFIG_USBH_LOG_LEVEL_OFF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_LOG_LEVEL_OFF)、[`CONFIG_USBH_LOG_LEVEL_ERR`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_LOG_LEVEL_ERR)、[`CONFIG_USBH_LOG_LEVEL_WRN`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_LOG_LEVEL_WRN)、[`CONFIG_USBH_LOG_LEVEL_INF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_LOG_LEVEL_INF)、[`CONFIG_USBH_LOG_LEVEL_DBG`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_LOG_LEVEL_DBG)。

<a id="CONFIG_USBH_LOG_LEVEL_DBG"></a>

## 379.33 `CONFIG_USBH_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机（usbh）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBH_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBH_LOG_LEVEL_DEFAULT"></a>

## 379.34 `CONFIG_USBH_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机（usbh）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBH_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBH_LOG_LEVEL_ERR"></a>

## 379.35 `CONFIG_USBH_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机（usbh）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBH_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBH_LOG_LEVEL_INF"></a>

## 379.36 `CONFIG_USBH_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机（usbh）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBH_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBH_LOG_LEVEL_OFF"></a>

## 379.37 `CONFIG_USBH_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机（usbh）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBH_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBH_LOG_LEVEL_WRN"></a>

## 379.38 `CONFIG_USBH_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBH_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机（usbh）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBH_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBH_UVC_LOG_LEVEL_CHOICE"></a>

## 379.39 `CONFIG_USBH_UVC_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB 主机视频类（usbh uvc）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USBH_VIDEO_CLASS && CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
CONFIG_USBH_UVC_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USBH_UVC_LOG_LEVEL_OFF
CONFIG_USBH_UVC_LOG_LEVEL_ERR
CONFIG_USBH_UVC_LOG_LEVEL_WRN
CONFIG_USBH_UVC_LOG_LEVEL_INF
CONFIG_USBH_UVC_LOG_LEVEL_DBG
CONFIG_USBH_UVC_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机视频类支持（host Video Class）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USBH_VIDEO_CLASS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBH_VIDEO_CLASS)、[`CONFIG_USB_HOST_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_HOST_STACK)、[`CONFIG_USBH_UVC_LOG_LEVEL_DEFAULT`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_UVC_LOG_LEVEL_DEFAULT)、[`CONFIG_USBH_UVC_LOG_LEVEL_OFF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_UVC_LOG_LEVEL_OFF)、[`CONFIG_USBH_UVC_LOG_LEVEL_ERR`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_UVC_LOG_LEVEL_ERR)、[`CONFIG_USBH_UVC_LOG_LEVEL_WRN`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_UVC_LOG_LEVEL_WRN)、[`CONFIG_USBH_UVC_LOG_LEVEL_INF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_UVC_LOG_LEVEL_INF)、[`CONFIG_USBH_UVC_LOG_LEVEL_DBG`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_UVC_LOG_LEVEL_DBG)。

<a id="CONFIG_USBH_UVC_LOG_LEVEL_DBG"></a>

## 379.40 `CONFIG_USBH_UVC_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBH_UVC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机视频类支持（host Video Class）【实验性 EXPERIMENTAL】 → USB 主机视频类（usbh uvc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBH_UVC_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_UVC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBH_UVC_LOG_LEVEL_DEFAULT"></a>

## 379.41 `CONFIG_USBH_UVC_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBH_UVC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机视频类支持（host Video Class）【实验性 EXPERIMENTAL】 → USB 主机视频类（usbh uvc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBH_UVC_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_UVC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBH_UVC_LOG_LEVEL_ERR"></a>

## 379.42 `CONFIG_USBH_UVC_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBH_UVC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机视频类支持（host Video Class）【实验性 EXPERIMENTAL】 → USB 主机视频类（usbh uvc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBH_UVC_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_UVC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBH_UVC_LOG_LEVEL_INF"></a>

## 379.43 `CONFIG_USBH_UVC_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBH_UVC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机视频类支持（host Video Class）【实验性 EXPERIMENTAL】 → USB 主机视频类（usbh uvc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBH_UVC_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_UVC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBH_UVC_LOG_LEVEL_OFF"></a>

## 379.44 `CONFIG_USBH_UVC_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBH_UVC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机视频类支持（host Video Class）【实验性 EXPERIMENTAL】 → USB 主机视频类（usbh uvc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBH_UVC_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_UVC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBH_UVC_LOG_LEVEL_WRN"></a>

## 379.45 `CONFIG_USBH_UVC_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBH_UVC_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → USB 主机视频类支持（host Video Class）【实验性 EXPERIMENTAL】 → USB 主机视频类（usbh uvc）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBH_UVC_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBH_UVC_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBIP_LOG_LEVEL_CHOICE"></a>

## 379.46 `CONFIG_USBIP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：通过 IP 的 USB 传输（usbip）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USBIP && CONFIG_USB_HOST_STACK
```

**默认值（Defaults）**

```text
CONFIG_USBIP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USBIP_LOG_LEVEL_OFF
CONFIG_USBIP_LOG_LEVEL_ERR
CONFIG_USBIP_LOG_LEVEL_WRN
CONFIG_USBIP_LOG_LEVEL_INF
CONFIG_USBIP_LOG_LEVEL_DBG
CONFIG_USBIP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → 通过 IP 传输 USB 的支持（USBIP）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USBIP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USBIP)、[`CONFIG_USB_HOST_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_HOST_STACK)、[`CONFIG_USBIP_LOG_LEVEL_DEFAULT`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBIP_LOG_LEVEL_DEFAULT)、[`CONFIG_USBIP_LOG_LEVEL_OFF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBIP_LOG_LEVEL_OFF)、[`CONFIG_USBIP_LOG_LEVEL_ERR`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBIP_LOG_LEVEL_ERR)、[`CONFIG_USBIP_LOG_LEVEL_WRN`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBIP_LOG_LEVEL_WRN)、[`CONFIG_USBIP_LOG_LEVEL_INF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBIP_LOG_LEVEL_INF)、[`CONFIG_USBIP_LOG_LEVEL_DBG`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBIP_LOG_LEVEL_DBG)。

<a id="CONFIG_USBIP_LOG_LEVEL_DBG"></a>

## 379.47 `CONFIG_USBIP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → 通过 IP 传输 USB 的支持（USBIP）【实验性 EXPERIMENTAL】 → 通过 IP 的 USB 传输（usbip）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBIP_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBIP_LOG_LEVEL_DEFAULT"></a>

## 379.48 `CONFIG_USBIP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → 通过 IP 传输 USB 的支持（USBIP）【实验性 EXPERIMENTAL】 → 通过 IP 的 USB 传输（usbip）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBIP_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBIP_LOG_LEVEL_ERR"></a>

## 379.49 `CONFIG_USBIP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → 通过 IP 传输 USB 的支持（USBIP）【实验性 EXPERIMENTAL】 → 通过 IP 的 USB 传输（usbip）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBIP_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBIP_LOG_LEVEL_INF"></a>

## 379.50 `CONFIG_USBIP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → 通过 IP 传输 USB 的支持（USBIP）【实验性 EXPERIMENTAL】 → 通过 IP 的 USB 传输（usbip）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBIP_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBIP_LOG_LEVEL_OFF"></a>

## 379.51 `CONFIG_USBIP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → 通过 IP 传输 USB 的支持（USBIP）【实验性 EXPERIMENTAL】 → 通过 IP 的 USB 传输（usbip）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBIP_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USBIP_LOG_LEVEL_WRN"></a>

## 379.52 `CONFIG_USBIP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USBIP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 主机协议栈（host stack）【实验性 EXPERIMENTAL】 → 通过 IP 传输 USB 的支持（USBIP）【实验性 EXPERIMENTAL】 → 通过 IP 的 USB 传输（usbip）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USBIP_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USBIP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_AUDIO_LOG_LEVEL_CHOICE"></a>

## 379.53 `CONFIG_USB_AUDIO_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB 音频（USB Audio）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USB_DEVICE_AUDIO && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
CONFIG_USB_AUDIO_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USB_AUDIO_LOG_LEVEL_OFF
CONFIG_USB_AUDIO_LOG_LEVEL_ERR
CONFIG_USB_AUDIO_LOG_LEVEL_WRN
CONFIG_USB_AUDIO_LOG_LEVEL_INF
CONFIG_USB_AUDIO_LOG_LEVEL_DBG
CONFIG_USB_AUDIO_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 音频设备类驱动（Audio Device Class Driver）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USB_DEVICE_AUDIO`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_AUDIO)、[`CONFIG_USB_DEVICE_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK)、[`CONFIG_USB_AUDIO_LOG_LEVEL_DEFAULT`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_AUDIO_LOG_LEVEL_DEFAULT)、[`CONFIG_USB_AUDIO_LOG_LEVEL_OFF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_AUDIO_LOG_LEVEL_OFF)、[`CONFIG_USB_AUDIO_LOG_LEVEL_ERR`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_AUDIO_LOG_LEVEL_ERR)、[`CONFIG_USB_AUDIO_LOG_LEVEL_WRN`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_AUDIO_LOG_LEVEL_WRN)、[`CONFIG_USB_AUDIO_LOG_LEVEL_INF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_AUDIO_LOG_LEVEL_INF)、[`CONFIG_USB_AUDIO_LOG_LEVEL_DBG`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_AUDIO_LOG_LEVEL_DBG)。

<a id="CONFIG_USB_AUDIO_LOG_LEVEL_DBG"></a>

## 379.54 `CONFIG_USB_AUDIO_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_AUDIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 音频设备类驱动（Audio Device Class Driver）【实验性 EXPERIMENTAL】 → USB 音频（USB Audio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_AUDIO_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_AUDIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_AUDIO_LOG_LEVEL_DEFAULT"></a>

## 379.55 `CONFIG_USB_AUDIO_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_AUDIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 音频设备类驱动（Audio Device Class Driver）【实验性 EXPERIMENTAL】 → USB 音频（USB Audio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_AUDIO_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_AUDIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_AUDIO_LOG_LEVEL_ERR"></a>

## 379.56 `CONFIG_USB_AUDIO_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_AUDIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 音频设备类驱动（Audio Device Class Driver）【实验性 EXPERIMENTAL】 → USB 音频（USB Audio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_AUDIO_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_AUDIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_AUDIO_LOG_LEVEL_INF"></a>

## 379.57 `CONFIG_USB_AUDIO_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_AUDIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 音频设备类驱动（Audio Device Class Driver）【实验性 EXPERIMENTAL】 → USB 音频（USB Audio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_AUDIO_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_AUDIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_AUDIO_LOG_LEVEL_OFF"></a>

## 379.58 `CONFIG_USB_AUDIO_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_AUDIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 音频设备类驱动（Audio Device Class Driver）【实验性 EXPERIMENTAL】 → USB 音频（USB Audio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_AUDIO_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_AUDIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_AUDIO_LOG_LEVEL_WRN"></a>

## 379.59 `CONFIG_USB_AUDIO_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_AUDIO_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 音频设备类驱动（Audio Device Class Driver）【实验性 EXPERIMENTAL】 → USB 音频（USB Audio）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_AUDIO_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_AUDIO_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_BC12_LOG_LEVEL_CHOICE"></a>

## 379.60 `CONFIG_USB_BC12_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB 电池充电规范 1.2（usb_bc12）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USB_BC12
```

**默认值（Defaults）**

```text
CONFIG_USB_BC12_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USB_BC12_LOG_LEVEL_OFF
CONFIG_USB_BC12_LOG_LEVEL_ERR
CONFIG_USB_BC12_LOG_LEVEL_WRN
CONFIG_USB_BC12_LOG_LEVEL_INF
CONFIG_USB_BC12_LOG_LEVEL_DBG
CONFIG_USB_BC12_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 电池充电规范 BC1.2 驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USB_BC12`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_BC12)、[`CONFIG_USB_BC12_LOG_LEVEL_DEFAULT`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_BC12_LOG_LEVEL_DEFAULT)、[`CONFIG_USB_BC12_LOG_LEVEL_OFF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_BC12_LOG_LEVEL_OFF)、[`CONFIG_USB_BC12_LOG_LEVEL_ERR`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_BC12_LOG_LEVEL_ERR)、[`CONFIG_USB_BC12_LOG_LEVEL_WRN`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_BC12_LOG_LEVEL_WRN)、[`CONFIG_USB_BC12_LOG_LEVEL_INF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_BC12_LOG_LEVEL_INF)、[`CONFIG_USB_BC12_LOG_LEVEL_DBG`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_BC12_LOG_LEVEL_DBG)。

<a id="CONFIG_USB_BC12_LOG_LEVEL_DBG"></a>

## 379.61 `CONFIG_USB_BC12_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_BC12_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 电池充电规范 BC1.2 驱动 → USB 电池充电规范 1.2（usb_bc12）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_BC12_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_BC12_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_BC12_LOG_LEVEL_DEFAULT"></a>

## 379.62 `CONFIG_USB_BC12_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_BC12_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 电池充电规范 BC1.2 驱动 → USB 电池充电规范 1.2（usb_bc12）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_BC12_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_BC12_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_BC12_LOG_LEVEL_ERR"></a>

## 379.63 `CONFIG_USB_BC12_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_BC12_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 电池充电规范 BC1.2 驱动 → USB 电池充电规范 1.2（usb_bc12）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_BC12_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_BC12_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_BC12_LOG_LEVEL_INF"></a>

## 379.64 `CONFIG_USB_BC12_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_BC12_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 电池充电规范 BC1.2 驱动 → USB 电池充电规范 1.2（usb_bc12）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_BC12_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_BC12_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_BC12_LOG_LEVEL_OFF"></a>

## 379.65 `CONFIG_USB_BC12_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_BC12_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 电池充电规范 BC1.2 驱动 → USB 电池充电规范 1.2（usb_bc12）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_BC12_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_BC12_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_BC12_LOG_LEVEL_WRN"></a>

## 379.66 `CONFIG_USB_BC12_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_BC12_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 电池充电规范 BC1.2 驱动 → USB 电池充电规范 1.2（usb_bc12）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_BC12_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_BC12_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_CDC_ACM_LOG_LEVEL_CHOICE"></a>

## 379.67 `CONFIG_USB_CDC_ACM_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB 通信类抽象控制模型（usb cdc acm）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USB_CDC_ACM && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
CONFIG_USB_CDC_ACM_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USB_CDC_ACM_LOG_LEVEL_OFF
CONFIG_USB_CDC_ACM_LOG_LEVEL_ERR
CONFIG_USB_CDC_ACM_LOG_LEVEL_WRN
CONFIG_USB_CDC_ACM_LOG_LEVEL_INF
CONFIG_USB_CDC_ACM_LOG_LEVEL_DBG
CONFIG_USB_CDC_ACM_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 通信设备类抽象控制模型支持（CDC ACM Class） → USB 通信设备类抽象控制模型支持（CDC ACM Class）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USB_CDC_ACM`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_CDC_ACM)、[`CONFIG_USB_DEVICE_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK)、[`CONFIG_USB_CDC_ACM_LOG_LEVEL_DEFAULT`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_CDC_ACM_LOG_LEVEL_DEFAULT)、[`CONFIG_USB_CDC_ACM_LOG_LEVEL_OFF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_CDC_ACM_LOG_LEVEL_OFF)、[`CONFIG_USB_CDC_ACM_LOG_LEVEL_ERR`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_CDC_ACM_LOG_LEVEL_ERR)、[`CONFIG_USB_CDC_ACM_LOG_LEVEL_WRN`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_CDC_ACM_LOG_LEVEL_WRN)、[`CONFIG_USB_CDC_ACM_LOG_LEVEL_INF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_CDC_ACM_LOG_LEVEL_INF)、[`CONFIG_USB_CDC_ACM_LOG_LEVEL_DBG`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_CDC_ACM_LOG_LEVEL_DBG)。

<a id="CONFIG_USB_CDC_ACM_LOG_LEVEL_DBG"></a>

## 379.68 `CONFIG_USB_CDC_ACM_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_CDC_ACM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 通信设备类抽象控制模型支持（CDC ACM Class） → USB 通信设备类抽象控制模型支持（CDC ACM Class） → USB 通信类抽象控制模型（usb cdc acm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_CDC_ACM_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_CDC_ACM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_CDC_ACM_LOG_LEVEL_DEFAULT"></a>

## 379.69 `CONFIG_USB_CDC_ACM_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_CDC_ACM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 通信设备类抽象控制模型支持（CDC ACM Class） → USB 通信设备类抽象控制模型支持（CDC ACM Class） → USB 通信类抽象控制模型（usb cdc acm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_CDC_ACM_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_CDC_ACM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_CDC_ACM_LOG_LEVEL_ERR"></a>

## 379.70 `CONFIG_USB_CDC_ACM_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_CDC_ACM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 通信设备类抽象控制模型支持（CDC ACM Class） → USB 通信设备类抽象控制模型支持（CDC ACM Class） → USB 通信类抽象控制模型（usb cdc acm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_CDC_ACM_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_CDC_ACM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_CDC_ACM_LOG_LEVEL_INF"></a>

## 379.71 `CONFIG_USB_CDC_ACM_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_CDC_ACM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 通信设备类抽象控制模型支持（CDC ACM Class） → USB 通信设备类抽象控制模型支持（CDC ACM Class） → USB 通信类抽象控制模型（usb cdc acm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_CDC_ACM_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_CDC_ACM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_CDC_ACM_LOG_LEVEL_OFF"></a>

## 379.72 `CONFIG_USB_CDC_ACM_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_CDC_ACM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 通信设备类抽象控制模型支持（CDC ACM Class） → USB 通信设备类抽象控制模型支持（CDC ACM Class） → USB 通信类抽象控制模型（usb cdc acm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_CDC_ACM_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_CDC_ACM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_CDC_ACM_LOG_LEVEL_WRN"></a>

## 379.73 `CONFIG_USB_CDC_ACM_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_CDC_ACM_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 通信设备类抽象控制模型支持（CDC ACM Class） → USB 通信设备类抽象控制模型支持（CDC ACM Class） → USB 通信类抽象控制模型（usb cdc acm）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_CDC_ACM_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_CDC_ACM_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_DEVICE_LOG_LEVEL_CHOICE"></a>

## 379.74 `CONFIG_USB_DEVICE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB 设备（usb device）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
CONFIG_USB_DEVICE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USB_DEVICE_LOG_LEVEL_OFF
CONFIG_USB_DEVICE_LOG_LEVEL_ERR
CONFIG_USB_DEVICE_LOG_LEVEL_WRN
CONFIG_USB_DEVICE_LOG_LEVEL_INF
CONFIG_USB_DEVICE_LOG_LEVEL_DBG
CONFIG_USB_DEVICE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USB_DEVICE_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK)、[`CONFIG_USB_DEVICE_LOG_LEVEL_DEFAULT`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_DEVICE_LOG_LEVEL_DEFAULT)、[`CONFIG_USB_DEVICE_LOG_LEVEL_OFF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_DEVICE_LOG_LEVEL_OFF)、[`CONFIG_USB_DEVICE_LOG_LEVEL_ERR`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_DEVICE_LOG_LEVEL_ERR)、[`CONFIG_USB_DEVICE_LOG_LEVEL_WRN`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_DEVICE_LOG_LEVEL_WRN)、[`CONFIG_USB_DEVICE_LOG_LEVEL_INF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_DEVICE_LOG_LEVEL_INF)、[`CONFIG_USB_DEVICE_LOG_LEVEL_DBG`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_DEVICE_LOG_LEVEL_DBG)。

<a id="CONFIG_USB_DEVICE_LOG_LEVEL_DBG"></a>

## 379.75 `CONFIG_USB_DEVICE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_DEVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 设备（usb device）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_DEVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_DEVICE_LOG_LEVEL_DEFAULT"></a>

## 379.76 `CONFIG_USB_DEVICE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_DEVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 设备（usb device）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_DEVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_DEVICE_LOG_LEVEL_ERR"></a>

## 379.77 `CONFIG_USB_DEVICE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_DEVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 设备（usb device）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_DEVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_DEVICE_LOG_LEVEL_INF"></a>

## 379.78 `CONFIG_USB_DEVICE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_DEVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 设备（usb device）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_DEVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_DEVICE_LOG_LEVEL_OFF"></a>

## 379.79 `CONFIG_USB_DEVICE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_DEVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 设备（usb device）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_DEVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_DEVICE_LOG_LEVEL_WRN"></a>

## 379.80 `CONFIG_USB_DEVICE_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_DEVICE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 设备（usb device）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_DEVICE_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_DEVICE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_DRIVER_LOG_LEVEL_CHOICE"></a>

## 379.81 `CONFIG_USB_DRIVER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB 驱动（usb driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USB_DEVICE_DRIVER
```

**默认值（Defaults）**

```text
CONFIG_USB_DRIVER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USB_DRIVER_LOG_LEVEL_OFF
CONFIG_USB_DRIVER_LOG_LEVEL_ERR
CONFIG_USB_DRIVER_LOG_LEVEL_WRN
CONFIG_USB_DRIVER_LOG_LEVEL_INF
CONFIG_USB_DRIVER_LOG_LEVEL_DBG
CONFIG_USB_DRIVER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USB_DEVICE_DRIVER`](P180_drivers_usb_配置项参考_2.md#CONFIG_USB_DEVICE_DRIVER)、[`CONFIG_USB_DRIVER_LOG_LEVEL_DEFAULT`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_DRIVER_LOG_LEVEL_DEFAULT)、[`CONFIG_USB_DRIVER_LOG_LEVEL_OFF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_DRIVER_LOG_LEVEL_OFF)、[`CONFIG_USB_DRIVER_LOG_LEVEL_ERR`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_DRIVER_LOG_LEVEL_ERR)、[`CONFIG_USB_DRIVER_LOG_LEVEL_WRN`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_DRIVER_LOG_LEVEL_WRN)、[`CONFIG_USB_DRIVER_LOG_LEVEL_INF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_DRIVER_LOG_LEVEL_INF)、[`CONFIG_USB_DRIVER_LOG_LEVEL_DBG`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_DRIVER_LOG_LEVEL_DBG)。

<a id="CONFIG_USB_DRIVER_LOG_LEVEL_DBG"></a>

## 379.82 `CONFIG_USB_DRIVER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → USB 驱动（usb driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_DRIVER_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_DRIVER_LOG_LEVEL_DEFAULT"></a>

## 379.83 `CONFIG_USB_DRIVER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → USB 驱动（usb driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_DRIVER_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_DRIVER_LOG_LEVEL_ERR"></a>

## 379.84 `CONFIG_USB_DRIVER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → USB 驱动（usb driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_DRIVER_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_DRIVER_LOG_LEVEL_INF"></a>

## 379.85 `CONFIG_USB_DRIVER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → USB 驱动（usb driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_DRIVER_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_DRIVER_LOG_LEVEL_OFF"></a>

## 379.86 `CONFIG_USB_DRIVER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → USB 驱动（usb driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_DRIVER_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_DRIVER_LOG_LEVEL_WRN"></a>

## 379.87 `CONFIG_USB_DRIVER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_DRIVER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → USB 设备控制器（Device Controller）驱动 → USB 驱动（usb driver）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_DRIVER_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_DRIVER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_HID_LOG_LEVEL_CHOICE"></a>

## 379.88 `CONFIG_USB_HID_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB 人机接口设备（usb hid）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USB_DEVICE_HID && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
CONFIG_USB_HID_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USB_HID_LOG_LEVEL_OFF
CONFIG_USB_HID_LOG_LEVEL_ERR
CONFIG_USB_HID_LOG_LEVEL_WRN
CONFIG_USB_HID_LOG_LEVEL_INF
CONFIG_USB_HID_LOG_LEVEL_DBG
CONFIG_USB_HID_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 人机接口设备支持（Human Interface Device）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USB_DEVICE_HID`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_HID)、[`CONFIG_USB_DEVICE_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK)、[`CONFIG_USB_HID_LOG_LEVEL_DEFAULT`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_HID_LOG_LEVEL_DEFAULT)、[`CONFIG_USB_HID_LOG_LEVEL_OFF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_HID_LOG_LEVEL_OFF)、[`CONFIG_USB_HID_LOG_LEVEL_ERR`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_HID_LOG_LEVEL_ERR)、[`CONFIG_USB_HID_LOG_LEVEL_WRN`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_HID_LOG_LEVEL_WRN)、[`CONFIG_USB_HID_LOG_LEVEL_INF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_HID_LOG_LEVEL_INF)、[`CONFIG_USB_HID_LOG_LEVEL_DBG`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_HID_LOG_LEVEL_DBG)。

<a id="CONFIG_USB_HID_LOG_LEVEL_DBG"></a>

## 379.89 `CONFIG_USB_HID_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_HID_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 人机接口设备支持（Human Interface Device） → USB 人机接口设备（usb hid）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_HID_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_HID_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_HID_LOG_LEVEL_DEFAULT"></a>

## 379.90 `CONFIG_USB_HID_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_HID_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 人机接口设备支持（Human Interface Device） → USB 人机接口设备（usb hid）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_HID_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_HID_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_HID_LOG_LEVEL_ERR"></a>

## 379.91 `CONFIG_USB_HID_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_HID_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 人机接口设备支持（Human Interface Device） → USB 人机接口设备（usb hid）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_HID_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_HID_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_HID_LOG_LEVEL_INF"></a>

## 379.92 `CONFIG_USB_HID_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_HID_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 人机接口设备支持（Human Interface Device） → USB 人机接口设备（usb hid）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_HID_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_HID_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_HID_LOG_LEVEL_OFF"></a>

## 379.93 `CONFIG_USB_HID_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_HID_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 人机接口设备支持（Human Interface Device） → USB 人机接口设备（usb hid）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_HID_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_HID_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_HID_LOG_LEVEL_WRN"></a>

## 379.94 `CONFIG_USB_HID_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_HID_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:14`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L14)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 人机接口设备支持（Human Interface Device） → USB 人机接口设备（usb hid）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_HID_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_HID_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_MASS_STORAGE_LOG_LEVEL_CHOICE"></a>

## 379.95 `CONFIG_USB_MASS_STORAGE_LOG_LEVEL_CHOICE`

**提示（Prompt）**：USB 大容量存储（usb mass storage）编译时纳入的最高日志级别（maximum compiled-in log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_USB_MASS_STORAGE && CONFIG_USB_DEVICE_STACK
```

**默认值（Defaults）**

```text
CONFIG_USB_MASS_STORAGE_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_USB_MASS_STORAGE_LOG_LEVEL_OFF
CONFIG_USB_MASS_STORAGE_LOG_LEVEL_ERR
CONFIG_USB_MASS_STORAGE_LOG_LEVEL_WRN
CONFIG_USB_MASS_STORAGE_LOG_LEVEL_INF
CONFIG_USB_MASS_STORAGE_LOG_LEVEL_DBG
CONFIG_USB_MASS_STORAGE_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:3`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L3)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 大容量存储设备类支持（Mass Storage Device Class）

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_USB_MASS_STORAGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_MASS_STORAGE)、[`CONFIG_USB_DEVICE_STACK`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_USB_DEVICE_STACK)、[`CONFIG_USB_MASS_STORAGE_LOG_LEVEL_DEFAULT`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_MASS_STORAGE_LOG_LEVEL_DEFAULT)、[`CONFIG_USB_MASS_STORAGE_LOG_LEVEL_OFF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_MASS_STORAGE_LOG_LEVEL_OFF)、[`CONFIG_USB_MASS_STORAGE_LOG_LEVEL_ERR`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_MASS_STORAGE_LOG_LEVEL_ERR)、[`CONFIG_USB_MASS_STORAGE_LOG_LEVEL_WRN`](P380_subsys_logging_配置项参考_29.md#CONFIG_USB_MASS_STORAGE_LOG_LEVEL_WRN)、[`CONFIG_USB_MASS_STORAGE_LOG_LEVEL_INF`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_MASS_STORAGE_LOG_LEVEL_INF)、[`CONFIG_USB_MASS_STORAGE_LOG_LEVEL_DBG`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_MASS_STORAGE_LOG_LEVEL_DBG)。

<a id="CONFIG_USB_MASS_STORAGE_LOG_LEVEL_DBG"></a>

## 379.96 `CONFIG_USB_MASS_STORAGE_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_MASS_STORAGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:20`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L20)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 大容量存储设备类支持（Mass Storage Device Class） → USB 大容量存储（usb mass storage）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_MASS_STORAGE_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_MASS_STORAGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_MASS_STORAGE_LOG_LEVEL_DEFAULT"></a>

## 379.97 `CONFIG_USB_MASS_STORAGE_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_MASS_STORAGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 大容量存储设备类支持（Mass Storage Device Class） → USB 大容量存储（usb mass storage）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_MASS_STORAGE_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_MASS_STORAGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_MASS_STORAGE_LOG_LEVEL_ERR"></a>

## 379.98 `CONFIG_USB_MASS_STORAGE_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_MASS_STORAGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 大容量存储设备类支持（Mass Storage Device Class） → USB 大容量存储（usb mass storage）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_MASS_STORAGE_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_MASS_STORAGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_MASS_STORAGE_LOG_LEVEL_INF"></a>

## 379.99 `CONFIG_USB_MASS_STORAGE_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_MASS_STORAGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:17`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L17)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 大容量存储设备类支持（Mass Storage Device Class） → USB 大容量存储（usb mass storage）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_MASS_STORAGE_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_MASS_STORAGE_LOG_LEVEL_CHOICE)。

<a id="CONFIG_USB_MASS_STORAGE_LOG_LEVEL_OFF"></a>

## 379.100 `CONFIG_USB_MASS_STORAGE_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_USB_MASS_STORAGE_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/logging/Kconfig.template.log_config:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/logging/Kconfig.template.log_config#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → USB 设备支持（Device Support）【已弃用 DEPRECATED】 → USB 大容量存储设备类支持（Mass Storage Device Class） → USB 大容量存储（usb mass storage）编译时纳入的最高日志级别（maximum compiled-in log level）

**配置项引用（Symbol References）**：[`CONFIG_USB_MASS_STORAGE_LOG_LEVEL_CHOICE`](P379_subsys_logging_配置项参考_28.md#CONFIG_USB_MASS_STORAGE_LOG_LEVEL_CHOICE)。

<!-- kconfig-navigation -->

[上一章](P378_subsys_logging_配置项参考_27.md) · [返回大纲](大纲.md) · [下一章](P380_subsys_logging_配置项参考_29.md)
